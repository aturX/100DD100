import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

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

# 用户加载回调函数
@login_manager.user_loader
def load_user(user_id):  # 创建用户加载回调函数，接受用户 ID 作为参数
	user = User.query.get(int(user_id))  # 用 ID 作为 User 模型的主键查询对应的用户
	return user   # 返回用户对象

@app.context_processor
def now_user():  # 函数名可以随意修改
	"""
	这个函数返回的变量（以字典键值对的形式）将会统一注入到每一个模板的上下文环境中，因此可以直接在模板中使用
	:return:
	"""
	user = User.query.first()

	return dict(user=user.name)  # 需要返回字典，等同于return {'user': user}




# 为了避免循环依赖（A 导入 B，B 导入 A），我们把这一行导入语句放到构造文件的结尾

from watchurls.models import User, Website
from watchurls import views, errors
