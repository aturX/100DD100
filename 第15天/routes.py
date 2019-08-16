

'''
	路由： 告诉用户 每个函数在哪里
'''

def template(filename):
	path = "templates/" + filename
	# 读取HTML页面的内容
	with open(path, 'r', encoding='utf-8') as f:
		content = f.read()
	return content
# print(template("login.html"))


def route_error():
	print("这是404 error函数")
	response = template("error.html")
	# HTTP响应的讲解
	response_head = 'HTTP / 1.1 200 OK\r\nContent - Type: text / html;\r\ncharset = utf-8\r\n\r\n'
	response = response_head + response
	return response.encode("utf-8")


def route_index():
	print("这是index函数")
	response = template("index.html")
	# HTTP响应的讲解
	response_head = 'HTTP / 1.1 200 OK\r\nContent - Type: text / html;\r\ncharset = utf-8\r\n\r\n'
	response = response_head + response
	return response.encode("utf-8")

def route_login():
	print("这是login函数")
	# if path == '/login':
	# response = "<html><head><meta content='text/html; charset=utf-8'></head><body>你在登陆页面了！</body></html>"
	response = template("login.html")
	# HTTP响应的讲解
	response_head = 'HTTP / 1.1 200 OK\r\nContent - Type: text / html;\r\ncharset = utf-8\r\n\r\n'
	response = response_head + response
	return response.encode("utf-8")

def get_img():
	path = "static/doge.gif"
	with open(path, 'rb') as f:
		response_head = b'HTTP / 1.1 200 OK\r\nContent-Type: image/gif\r\n\r\n'
		img = response_head + f.read()
	return img

route_dict = {
	"/": route_index,
	"/login": route_login,
	"/static/doge.gif": get_img
}