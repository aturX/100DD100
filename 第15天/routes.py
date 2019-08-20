

'''
	路由： 告诉用户 每个函数在哪里
'''
from models import save, load, User
from utils import log


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
	print("这是login函数")
	# if path == '/login':
	# response = "<html><head><meta content='text/html; charset=utf-8'></head><body>你在登陆页面了！</body></html>"
	response = template("login.html")
	# HTTP响应的讲解
	response_head = 'HTTP / 1.1 200 OK\r\nContent - Type: text / html;\r\ncharset = utf-8\r\n\r\n'
	response = response_head + response
	return response.encode("utf-8")

def get_img(request):
	path = "static/doge.gif"
	with open(path, 'rb') as f:
		response_head = b'HTTP / 1.1 200 OK\r\nContent-Type: image/gif\r\n\r\n'
		img = response_head + f.read()
	return img

def dologin(request):
	log("dologin path", request.path)
	log("dologin query", request.query["user"])

	# 用户信息应该取自文件
	loginData = load("./db/User.txt")

	log("loginData", loginData)

	user = "admin"
	password = "admin123"
	r = b'HTTP / 1.1 200 OK\r\nContent - Type: text / html;\r\ncharset = utf-8\r\n\r\nlogin fail!'
	if user == request.query["user"] and password == request.query["password"]:
		r = route_index(request)
	# HTTP响应的讲解
	return r

def doregister(request):
	log(request.query["rName"])
	log(request.query["rPassword"])
	# 注册信息 要写入 数据存储中 （数据库、缓存、文件）
	if len(request.query["rName"]) > 1 and len(request.query["rPassword"]) > 1:
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
	"/": route_login,
	"/home": route_index,
	"/register": route_register,
	"/static/doge.gif": get_img,
	"/dologin": dologin,
	"/doregister": doregister,
	"/doregisterPost": doregister_post
}