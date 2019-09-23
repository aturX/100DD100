from flask import Flask, url_for

"""
 路由的生产与使用
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




if __name__ == "__main__":
	app.run(host="0.0.0.0", port="6666")

