

from flask import Flask, url_for, request, render_template, make_response
from werkzeug.utils import secure_filename

from utils import valid_login, log_the_user_in

"""
 上传文件 
 
 1. HTML  表单 设置属性  enctype=multipart/form-data
 2. 指定form表单提交  写好路由
 3.  文件写到本地服务器  f.save('/var/www/uploads/' + secure_filename(f.filename))
  
 
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


# 8. 模板渲染
@app.route('/template/')
@app.route('/template/<name>')
def template_hello(name=None):
	return render_template('hello.html', name=name)

"""
模板里，你也可以访问 request 、 session 和 g [1] 对象

"""
# 9. 自动转义功能  Markup  标记HTML字符串 且在页面进行转义
@app.route('/markup')
def markup():
	from flask import Markup
	s = "<strong style='color:red'>Hello {}!</strong>".format("你好！")
	news = Markup(s)
	return render_template('hello.html', news=news)

# 10. request 实现测试 controller
@app.route('/test')
def test_route():
	from flask import request
	with app.test_request_context('/hello', method='POST'):
		# now you can do something with the request until the
		# end of the with block, such as basic assertions:
		assert request.path == '/hello'
		assert request.method == 'POST'

	return "success"


# 11. request 实现 登录功能 form表单提交
@app.route('/dologin', methods=['POST', 'GET'])
def do_login():
	error = ""
	if request.method == 'POST':
		if valid_login(request.form['username'],
		               request.form['password']):
			return log_the_user_in(request.form['username'])
		else:
			error = '用户名或密码错误 username/password'

	"""
	通过 args 属性来访问 URL 中提交的参数 （ ?key=value ）
	searchword = request.args.get('q', '')
	"""
	return render_template('hello.html', error=error)

# 12 上传文件
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		f.save('./upload/' + secure_filename(f.filename))
	return "success"

# 13.1 初次登录 Cookies 状态设定  set-cookie
@app.route('/setcookie', methods=['GET', 'POST'])
def set_cookie_login():
	if valid_login(request.form['username'],
		    request.form['password']):
		response = make_response(render_template('hello.html', username=request.form['username']))
		response.set_cookie('username', request.form['username'])
		return response
	else:
		error = '用户名或密码错误 username/password'
		return render_template('hello.html', username=error)


# 13.2 Cookies 登录状态保留
@app.route('/cookie', methods=['GET', 'POST'])
def cookie_login():
	username = request.cookies.get('username', '')  # 如果有cookies 且该用户登录过则显示，否则显示游客
	if username == '':
		return render_template('hello.html', cookie_user="游客")
	else:
		return render_template('hello.html', cookie_user=username)


if __name__ == "__main__":
	app.run(host="0.0.0.0", port="6666")

