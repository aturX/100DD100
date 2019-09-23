from flask import Flask, url_for, request

"""
 HTTP 方法 
 
 主要常用：  GET  POST
 
"""
app = Flask(__name__)

# 1. 路由访问
@app.route('/')
def hello_flask():
	return 'hello flask'

# 2. 路由路径访问
@app.route('/path')
def hello_path():
	return 'hello path'

# 3. path 传参
@app.route('/path/<username>')
def hello_username(username):
	return 'hello {}'.format(username)


# 4. 动态生成路由 （复杂场景必须的功能）
@app.route('/create')
def create_url():
	with app.test_request_context():
		print(url_for('hello_flask'))
		print(url_for('hello_path'))
		print(url_for('hello_username', username='lsy'))
		print(url_for('hello_username', username='John Doe'))
	return "success"

# 5. HTTP方法   POST请求
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		print("完成登录的逻辑！")
		return "登录成功！"
	else:
		print("重新刷页面，回到登录页面!")
		return "登录失败， 重新登录"

# 6. HTTP方法   GET请求
@app.route('/sayhello/<username>', methods=['GET', 'POST'])
def say_hello(username):
	if request.method == 'GET':
		print("你好 {}！".format(username))
		print(request)
		return "你好 {}！".format(username)
	else:
		print("重新刷页面，回到登录页面!")
		return "登录失败， 重新登录"

# 7. 静态文件生成URL
@app.route('/static/')
def create_static_url():
	url = (url_for('static', filename='style.css'))
	return url

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="6666")

