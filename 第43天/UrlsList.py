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


TODO - 待办

- 模板继承机制



"""
import os
import sys

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# 关于数据库的配置 及初始化

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

db = init_db(app)
# 用户模型
class User(db.Model):   # 表名将会是 user（自动生成，小写处理）
	# 主键 id
	id = db.Column(db.Integer, primary_key=True)  # 主键
	name = db.Column(db.String(20))  # 名字

# 网站信息模型
class Website(db.Model):  # 表明 website
	id = db.Column(db.Integer, primary_key=True)  # 主键
	name = db.Column(db.String(40))   # 网站名字
	url = db.Column(db.String(128))   # 网址
	info = db.Column(db.String(128))  # 介绍信息

# 模板上下文函数
@app.context_processor
def now_user():  # 函数名可以随意修改
	"""
	这个函数返回的变量（以字典键值对的形式）将会统一注入到每一个模板的上下文环境中，因此可以直接在模板中使用
	:return:
	"""
	user = User.query.first()

	return dict(user=user.name)  # 需要返回字典，等同于return {'user': user}




@app.route('/')
@app.route('/index')
def index():
	# 读取数据库
	# name = User.query.first().name  # 读取用户记录
	websites = Website.query.all()  # 查询全部网站数据
	return render_template('index.html', websites=websites)

# 404 问题
@app.errorhandler(404)
def page_not_found(e):
	# user = User.query.first()  # 读取用户记录
	return render_template('404.html'), 404  # 返回模板和状态码

# 在子模板里，我们可以使用 extends 标签来声明继承自某个基模板


if __name__ == "__main__":
	app.run(host="0.0.0.0", port="6666")