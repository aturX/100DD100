

'''
	路由： 告诉用户 每个函数在哪里
'''
from models import save, load, User
from utils import log, random_str

message_list = []  # 所有消息
session = {}   # 记录所有session会话 状态


def response_with_headers(headers):
    """
Content-Type: text/html
Set-Cookie: user=gua
    """
    header = 'HTTP/1.1 200 OK\r\n'
    header += ''.join(['{}: {}\r\n'.format(k, v)
                           for k, v in headers.items()])
    return header

# 有cookie 可识别当前用户, 服务器留存session
def current_user(request):
	# 自定义 session 记录方式
	session_id = request.cookies.get('visiter', '')  # 如果第一次访问 无，则为空
	username = session.get(session_id, '游客')
	return username



def template(filename):
	path = "templates/" + filename
	# 读取HTML页面的内容
	with open(path, 'r', encoding='utf-8') as f:
		content = f.read()
	return content
# print(template("login.html"))


def route_error(request):
	print("这是404 error函数")
	response = template("error.html")
	# HTTP响应的讲解
	response_head = 'HTTP / 1.1 200 OK\r\nContent - Type: text / html;\r\ncharset = utf-8\r\n\r\n'
	response = response_head + response
	return response.encode("utf-8")


def route_index(request):
	print("这是index函数")
	response = template("index.html")
	# HTTP响应的讲解
	response_head = 'HTTP / 1.1 200 OK\r\nContent - Type: text / html;\r\ncharset = utf-8\r\n\r\n'
	response = response_head + response
	return response.encode("utf-8")

def route_login(request):
	"""
	登录页面 完成cookie 认证
	:param request:
	:return:
	"""
	# 告诉浏览器一些信息
	headers = {
		'Content-Type': 'text/html',
	}

	log("login cookies", request.cookies)
	username = current_user(request)
	if request.method == "POST":
		form = request.form()   # form 表单   ?a=1&b=2
		log(" form  username", type(form), form.get('username', ''))
		log(" form  password", type(form), form.get('password', ''))
		u = User.new(form)
		if u.validate_login():
			session_id = random_str()    # 登录的用户给一个session id
			session[session_id] = u.username  # 每个session id  对应一个用户
			# 给浏览器分配一个cookie
			headers['Set-Cookie'] = 'visiter={}'.format(session_id)
			body = template("index.html")
			body = body.replace('{{result}}', '登录成功！')
			body = body.replace('{{username}}', username)

			# 构造响应的header
			header = response_with_headers(headers)

			response = header + '\r\n' + body
			return response.encode("utf-8")
		else:
			response = template("login.html")
			# if path == '/login':
			# response = "<html><head><meta content='text/html; charset=utf-8'></head><body>你在登陆页面了！</body></html>"
			response = response.replace('{{result}}', '登录失败！')
			response = response.replace('{{username}}', username)
			# HTTP响应的讲解
			response_head = 'HTTP / 1.1 200 OK\r\nContent - Type: text / html;\r\ncharset = utf-8\r\n\r\n'
			response = response_head + response
			return response.encode("utf-8")
	else:
		u = User.new(request.query)
		session_id = random_str()  # 登录的用户给一个session id
		session[session_id] = u.username  # 每个session id  对应一个用户
		# 给浏览器分配一个cookie
		headers['Set-Cookie'] = 'visiter={}'.format(session_id)
		response_head = 'HTTP / 1.1 200 OK\r\nContent - Type: text / html;\r\ncharset = utf-8\r\n\r\n'
		response = template("login.html")
		response = response.replace('{{result}}', '')
		response = response.replace('{{username}}', username)
		response = response_head + response
		return response.encode("utf-8")

def get_img(request):
	path = "static/doge.gif"
	with open(path, 'rb') as f:
		response_head = b'HTTP / 1.1 200 OK\r\nContent-Type: image/gif\r\n\r\n'
		img = response_head + f.read()
	return img

def dologin(request):
	# 用户信息应该取自文件
	loginData = load("./db/User.txt")
	log("loginData", loginData)

	user = loginData["username"]
	password = loginData["password"]
	r = b'HTTP / 1.1 200 OK\r\nContent - Type: text / html;\r\ncharset = utf-8\r\n\r\nlogin fail!'
	if user == request.query["user"] and password == request.query["password"]:
		r = route_index(request)
	# HTTP响应的讲解
	return r

def doregister(request):
	# 注册信息 要写入 数据存储中 （数据库、缓存、文件）
	if len(request.query["username"]) > 1 and len(request.query["password"]) > 1:
		r = route_index(request)
		# 注册数据保存
		save(request.query, "db/User.txt")
	else:
		r = b'HTTP / 1.1 200 OK\r\nContent - Type: text / html;\r\ncharset = utf-8\r\n\r\nregister fail!'
	return r

def doregister_post(request):
	header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
	log("******Method******", request.method)
	if request.method == 'POST':
		form = request.form()
		u = User.new(form)
		if u.validate_register():
			u.save()
			result = '注册成功<br> <pre>{}</pre>'.format(User.all())
		else:
			result = '用户名长度必须大于1'
	else:
		result = ''
	body = template('register.html')
	body = body.replace('{{result}}', result)  # 模板的作用
	r = header + body
	log("r", r)
	return r.encode('utf-8')

def route_register(request):
	# 用户注册
	response = template("register.html")
	# HTTP响应的讲解
	response_head = 'HTTP / 1.1 200 OK\r\nContent - Type: text / html;\r\ncharset = utf-8\r\n\r\n'
	response = response_head + response
	return response.encode("utf-8")

route_dict = {
	# "/": route_login,
	"/home": route_index,
	"/register": route_register,
	"/login": route_login,
	"/static/doge.gif": get_img,
	"/dologin": dologin,
	"/doregister": doregister,
	"/doregisterPost": doregister_post
}