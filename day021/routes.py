import random

# 这个函数用来保存所有的 messages
from models import User, Message

message_list = []
# session 可以在服务器端实现过期功能
session = {}

def random_str():
	"""
	生成一个随机的字符串
	"""
	seed = 'abcdefjsad89234hdsfkljasdkjghigaksldf89weru'
	s = ''
	for i in range(16):
		# 这里 len(seed) - 2 是因为我懒得去翻文档来确定边界了
		random_index = random.randint(0, len(seed) - 2)
		s += seed[random_index]
	return s


def template(name):
	path = 'templates/' + name
	with open(path, 'r', encoding='utf-8') as f:
		return f.read()

def current_user(request):
	session_id = request.cookies.get('user', '')
	username = session.get(session_id, '【游客】')
	return username


def route_index(request):
	"""
	主页的处理函数, 返回主页的响应
	"""
	header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
	body = template('index.html')
	username = current_user(request)
	body = body.replace('{{username}}', username)
	r = header + '\r\n' + body
	return r.encode(encoding='utf-8')


def response_with_headers(headers, code=200):
	header = 'HTTP/1.1 {} Very OK\r\n'.format(code)
	header += ''.join(['{}: {}\r\n'.format(k, v) for k, v in headers.items()])
	print('header', header)
	return header


# 重定向添加函数
def redirect(url):
	"""
	浏览器在收到 302 响应的时候
	会自动在 HTTP header 里面找 Location 字段并获取一个 url
	然后自动请求新的 url
	"""
	headers = {
		'Location': url,
	}
	# 增加 Location 字段并生成 HTTP 响应返回
	# 注意, 没有 HTTP body 部分
	r = response_with_headers(headers, 302) + '\r\n'
	return r.encode('utf-8')


# 登录
def route_login(request):
	headers = {
		 'Content-Type': 'text/html',
	}
	username = current_user(request)
	if request.method == 'POST':
		form = request.form()
		u = User.new(form)
		if u.validate_login():
			# 设置一个随机字符串来当令牌使用
			session_id = random_str()
			session[session_id] = u.username
			headers['Set-Cookie'] = 'user={}'.format(session_id)
			result = '登录成功'
		else:
			result = '用户名或者密码错误'
	else:
		result = ''
	body = template('login.html')
	body = body.replace('{{result}}', result)
	body = body.replace('{{username}}', username)
	header = response_with_headers(headers)
	r = header  + '\r\n' + body
	return r.encode(encoding='utf-8')


# 注册
def route_register(request):
	"""
	注册页面的路由函数
	"""
	header = 'HTTP/1.1 210 VERY OK\r\nContent-Type: text/html\r\n'
	if request.method == 'POST':
		form = request.form()
		u = User.new(form)
		if u.validate_register():
			u.save()
			result = '注册成功<br> <pre>{}</pre>'.format(User.all())
		else:
			result = '用户名或者密码长度必须大于2'
	else:
		result = ''
	body = template('register.html')
	body = body.replace('{{result}}', result)
	r = header + '\r\n' + body
	return r.encode(encoding='utf-8')
# 信息
def route_message(request):
	"""
	消息页面的路由函数
	"""
	username = current_user(request)
	# 如果是未登录的用户, 重定向到 '/'
	if username == '【游客】':
		return redirect('/')
	if request.method == 'POST':
		form = request.form()
		msg = Message.new(form)

		message_list.append(msg)
		# 应该在这里保存 message_list
	header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'

	body = template('html_basic.html')
	# 构造消息 HTML 标签
	msgs = '<br>'.join([str(m) for m in message_list])
	body = body.replace('{{messages}}', msgs)
	r = header + '\r\n' + body
	return r.encode(encoding='utf-8')

# 图片资源加载
def route_static(request):
	"""
	静态资源的处理函数, 读取图片并生成响应返回
	"""
	filename = request.query.get('file', 'doge.gif')
	path = 'static/' + filename
	with open(path, 'rb') as f:
		header = b'HTTP/1.1 200 OK\r\nContent-Type: image/gif\r\n\r\n'
		img = header + f.read()
		return img


def test_redirect(request):
	return redirect('/login')


# 路由字典
# key 是路由(路由就是 path)
# value 是路由处理函数(就是响应)
route_dict = {
    '/': route_index,
    '/login': route_login,
    '/register': route_register,
    '/messages': route_message,
	'/test': test_redirect,
}