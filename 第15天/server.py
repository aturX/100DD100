import urllib.parse
from time import sleep
import socket
import routes
from utils import log


class Request(object):
	def __init__(self):
		self.method = 'GET'
		self.path = ''
		self.query = ''
		self.body = ''

	def form(self):
		# body = urllib.parse.unquote("python%26%26%26%26")
		body = urllib.parse.unquote(self.body)
		args = body.split('&')
		f = {}
		log("args---------",args)
		for arg in args:
			k, v = arg.split("=")
			f[k] = v
		return f


def parsed_path(path):
	log("parsed_path", path)
	index = path.find('?')
	if index == -1:
		return path,{}
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
	# 写入到全局变量request中
	request.method = method
	request.body = body
	request.path, request.query = parsed_path(path)
	response = routes.route_dict.get(request.path, routes.route_error)
	log("*********", request.path, request.query)
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
			request = connect.recv(1000)
			request = request.decode('utf-8')
			print(request)
			# print(request.split('\r\n')[0])
			# print(request.split('\r\n')[0].split(' ')[1])
			# print(request.split('\r\n')[0].split(' ')[0])
			if len(request.split()) < 2:
				continue
			path = request.split('\r\n')[0].split(' ')[1]
			method = request.split('\r\n')[0].split(' ')[0]

			# 解析 path
			# response = "你要啥 我不知道"
			# response = "？"
			response = response_for_path(request)

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
		"port": 3000
	}
	run(**config)


