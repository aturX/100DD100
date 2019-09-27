"""
Flask 入门项目：
网站内容信息展示 UrlsList
参考：  http://watchlist.helloflask.com/
教程： https://read.helloflask.com/c1-ready

Done - 完成
- 完成  浏览器 编辑器 开发工具 ： Chrome  + Pycharm + Python3.7 + Flask + Pipenv + Git + Linux （Vim）
- 完成  配置虚拟环境 安装web框架  提交代码版本控制 ： Pipenv + Flask + GitHub
- 完成  配置Flask 的配置文件 .env .flaskenv  使用 python-dotenv
- 完成  使用模板基础 ： 模板基本语法
- 完成  编写主页模板
- 完成  准备虚拟数据
- 完成  渲染主页模板
- 完成  连接使用数据库
- 完成  使用ORM框架SQLAlchemy
- 完成  创建表映射 类class
- 完成  模板上下文环境
- 完成  模板继承机制
- 完成  表单提交 登录功能
- 完成  消息反馈
- 完成  编辑条目 添加内容
- 完成  删除条目
- 完成  安全存储密码
- 完成  生成管理员账户
- 完成  使用Flask-Login 实现用户认证
- 完成  登录登出功能实现
- 完成  认证保护

TODO - 待办

-




"""
import os
import sys

from flask import Flask, render_template, request, flash, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from flask_sqlalchemy import SQLAlchemy

# 关于数据库的配置 及初始化
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect


def init_db(app):
	# ORM 框架
	# sqlite 的写法  sqlite:////数据库文件的绝对地址（Linux）  sqlite:///数据库文件的绝对地址 （windows）
	WIN = sys.platform.startswith('win')
	if WIN:  # 如果是 Windows 系统，使用三个斜线
		prefix = 'sqlite:///'
	else:  # 否则使用四个斜线
		prefix = 'sqlite:////'
	app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'db/data.db')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
	db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app
	return db

app = Flask(__name__)
app.secret_key = "adfaksdhfk^&*^(%&^%"
db = init_db(app)

login_manager = LoginManager(app)  # 实例化扩展类
login_manager.login_view = 'login'   # 登录视图端点（函数名）

# 用户模型
class User(db.Model,UserMixin):   # 表名将会是 user（自动生成，小写处理）
	# 主键 id
	id = db.Column(db.Integer, primary_key=True)  # 主键
	name = db.Column(db.String(20))  # 名字
	username = db.Column(db.String(20))  # 用户名
	password_hash = db.Column(db.String(128))  # 密码散列值


	def set_password(self, password):
		self.password_hash = generate_password_hash(password)  # 将生成的密码保持到对应字段

	def validate_password(self, password):  # 用于验证密码的方法，接受密码作为参数
		return check_password_hash(self.password_hash, password)  # 返回布尔值

# 网站信息模型
class Website(db.Model):  # 表明 website
	id = db.Column(db.Integer, primary_key=True)  # 主键
	name = db.Column(db.String(40))   # 网站名字
	url = db.Column(db.String(128))   # 网址
	info = db.Column(db.String(128))  # 介绍信息


# 用户加载回调函数
@login_manager.user_loader
def load_user(user_id):  # 创建用户加载回调函数，接受用户 ID 作为参数
	user = User.query.get(int(user_id))  # 用 ID 作为 User 模型的主键查询对应的用户
	return user   # 返回用户对象






# 模板上下文函数
@app.context_processor
def now_user():  # 函数名可以随意修改
	"""
	这个函数返回的变量（以字典键值对的形式）将会统一注入到每一个模板的上下文环境中，因此可以直接在模板中使用
	:return:
	"""
	user = User.query.first()

	return dict(user=user.name)  # 需要返回字典，等同于return {'user': user}


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	# 读取数据库
	if request.method == 'POST':  # 判断是否是 POST 请求
		if not current_user.is_authenticated:  # 如果当前用户未认证
			return redirect(url_for('index'))  # 重定向到主页
		name = request.form.get('name')
		url = request.form.get('url')
		# 验证数据
		if len(name) < 1 or len(url) < 1:
			flash('信息填写错误！')  # 显示错误提示
			return redirect(url_for('index'))  # 重定向回主页
		# 保存表单数据到数据库
		website = Website(name=name, url=url)  # 创建记录
		db.session.add(website)  # 添加到数据库会话
		db.session.commit()  # 提交数据库会话
		flash('网址添加成功！')  # 显示成功创建的提示
		return redirect(url_for('index'))  # 重定向回主页
	# name = User.query.first().name  # 读取用户记录
	websites = Website.query.all()  # 查询全部网站数据
	return render_template('index.html', websites=websites)

# 404 问题
@app.errorhandler(404)
def page_not_found(e):
	# user = User.query.first()  # 读取用户记录
	return render_template('404.html'), 404  # 返回模板和状态码

# 在子模板里，我们可以使用 extends 标签来声明继承自某个基模板

# 编辑网站内容
@app.route('/website/edit/<int:website_id>', methods=['GET', 'POST'])
@login_required  # 登录保护
def edit(website_id):
	website = Website.query.get_or_404(website_id)
	# GET 和 POST 在同一路由中使用
	if request.method == 'POST':  # 处理编辑表单的提交请求
		name = request.form['name']
		url = request.form['url']
		if len(name) < 1 or len(url) < 1:
			flash('信息填写错误！')
			return redirect(url_for('edit', website_id=website_id))  # 重定向回对应的编辑页面

		website.name = name  # 更新名称
		website.url = url  # 更新网址
		db.session.commit()  # 提交数据库会话
		flash('修改成功！')
		return redirect(url_for('index'))  # 重定向回主页

	return render_template('edit.html', website=website)  # 传入被编辑的电影记录


@app.route('/website/delete/<int:website_id>', methods=['POST'])
@login_required  # 登录保护
def delete(website_id):
	movie = Website.query.get_or_404(website_id)  # 获取记录
	db.session.delete(movie)  # 删除对应的记录
	db.session.commit()  # 提交数据库会话
	flash('删除成功！')
	return redirect(url_for('index'))  # 重定向回主页



# --------------------------  Login  ---------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		if not username or not password:
			flash('输入错误！')
			return redirect(url_for('login'))

		user = User.query.first()
		# 验证用户名和密码是否一致
		if username == user.username and user.validate_password(password):
			login_user(user)  # 登入用户  (Flask-login的插件)
			flash('登录成功！')
			return redirect(url_for('index'))  # 重定向到主页
		flash('输入用户名或密码错误！')  # 如果验证失败，显示错误消息
		return redirect(url_for('login'))  # 重定向回登录页面

	return render_template('login.html')

# -------------------------- Logout ----------------------------------
@app.route('/logout')
@login_required  # 用于视图保护，后面会详细介绍
def logout():
	logout_user()  # 登出用户
	flash('已退出！')
	return redirect(url_for('index'))  # 重定向回首页

# 对于不允许未登录用户访问的视图，只需要为视图函数附加一个 login_required 装饰器就可以将未登录用户拒之门外

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
	if request.method == 'POST':
		name = request.form['name']

		if not name or len(name) > 20:
			flash('Invalid input.')
			return redirect(url_for('settings'))

		current_user.name = name
		# current_user 会返回当前登录用户的数据库记录对象
		# 等同于下面的用法
		# user = User.query.first()
		# user.name = name
		db.session.commit()
		flash('Settings updated.')
		return redirect(url_for('index'))
	return render_template('settings.html')




if __name__ == "__main__":
	app.run(host="0.0.0.0", port="6666")