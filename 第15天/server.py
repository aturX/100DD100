import urllib.parse
from time import sleep
import socket
import routes
from utils import log


class Request(object):
	"""
	1. headers   请求头
	2. body
	3. query
	4. path
	5. method
	"""
	def __init__(self):
		self.method = 'GET'
		self.path = ''
		self.query = {}
		self.body = ''
		self.headers = {}
		self.cookies = {}

	# 第一次访问是没有cookies的
	def add_cookies(self):
		# 为头部添加cookies (本质： 字符串结构化处理)
		'''
		[
            'Cookie: height=111; user=222'
        ]
		Cookie 的套路
		'''
		# 1. 从请求中获取Cookie 如果存在的话
		cookies = self.headers.get('Cookie', '')
		kvs = cookies.split('; ')
		for kv in kvs:
			if '=' in kv:
				k, v = kv.split('=')
				self.cookies[k] = v

	# headers 的结构化  字符串 -> 数据结构
	def add_headers(self, header):
		"""
	        获取头部信息
	        Accept-Language: zh-CN,zh;q=0.8
	        Cookie: height=1221; user=lsy
		 """
		lines = header
		for line in lines:
			k, v = line.split(': ', 1)
			self.headers[k] = v
		# 请求中的headers 都写入 对象 并新增cookies
		self.add_cookies()

	def form(self):
		# body = urllib.parse.unquote("python%26%26%26%26")
		body = urllib.parse.unquote(self.body)
		args = body.split('&')
		f = {}
		for arg in args:
			k, v = arg.split("=")
			f[k] = v
		return f


def parsed_path(path):
	log("parsed_path", path)
	index = path.find('?')
	if index == -1:
		return path, {}
	else:
		request_path = path.split("?")[0]
		log("request_path", request_path)
		request_query = path.split("?")[1].split("&")
		query = {}
		for arg in request_query:
			k, v = arg.split('=')
			query[k] = v
		return request_path, query


def response_for_path(_request):
	# print(routes.route_dict)
	# print(routes.route_dict["/login"]())
	# print(routes.route_dict[path]())
	# response = routes.route_dict[path]()
	# 解析 path
	method = _request.split('\r\n')[0].split(' ')[0]
	path = _request.split('\r\n')[0].split(' ')[1]
	body = _request.split('\r\n\r\n')[1]
	request.add_headers(_request.split('\r\n\r\n', 1)[0].split('\r\n')[1:])
	# 写入到全局变量request中
	request.method = method
	request.body = body
	request.path, request.query = parsed_path(path)
	response = routes.route_dict.get(request.path, routes.route_error)
	log("***************************", _request.split('\r\n\r\n', 1)[0].split('\r\n')[1:])
	log("***************************", request.headers,request.cookies)
	# return response()
	return response(request)

# response_for_path("/loginggg")


def run(host, port):
	# 启动服务器

	# 《网络是怎么连接的？》 第一章
	# socket 1. 创建socket 2. 建立socket connect 连接 3. 监听等待连接请求（服务器）， 向连接发送请求（客户端）
	# 4. 根据请求，返回给客户端响应 （服务端）， 得到客户端返回的响应 （客户端） 5. 关闭连接
	# 我们现在的 web框架的角色是 （服务端 server.py）

	# 1、 创建socket
	with socket.socket() as s:
		# 2、 建立socket connect 连接 : python 是建立在操作系统上的， 必须绑定在一个端口上，才能发送网络信息
		print("启动服务器: 项目上线 " + "http://" + host + ":" + str(port))
		s.bind((host, port))

		while True:
		# 3. 监听等待连接请求（服务器）
			print("开启服务器监听...")
			s.listen()
			connect, address = s.accept()
			# print(connect.recv(1000))
			r = connect.recv(1000)
			r = r.decode('utf-8')
			print(r)
			# print(request.split('\r\n')[0])
			# print(request.split('\r\n')[0].split(' ')[1])
			# print(request.split('\r\n')[0].split(' ')[0])
			if len(r.split()) < 2:
				continue

			# 解析 path
			# response = "你要啥 我不知道"
			# response = "？"
			response = response_for_path(r)

		# 4、 返回给 用户的需求
			connect.sendall(response)  # Accept: text/html
			connect.close()
			sleep(3)


request = Request()

if __name__ == '__main__':
	# 启动服务器 需要一个端口
	# host = "lisiyi.top"
	# port = 3000
	config = {
		# "host": "lisiyi.top",
		"host": "localhost",
		"port": 4000
	}
	run(**config)


