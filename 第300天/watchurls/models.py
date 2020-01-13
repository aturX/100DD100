from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash




# 用户模型
from watchurls import db


class User(db.Model, UserMixin):   # 表名将会是 user（自动生成，小写处理）
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



















def test_add_user():
	# 添加一个用户
	user = User(name='Lsy')

	# 写入数据库
	db.session.add(user)  # 把新创建的记录添加到数据库会话

	# 创建一个Website 记录
	web = Website(name='百度', url='http://www.baidu.com', info='搜索引擎')

	db.session.add(web)

	# 保存 确认 并提交
	db.session.commit()


def test_query_user():
	users = User.query.all()
	print(users[0].name)

	user_first = User.query.first()
	print(user_first.name)

	user_first1 = User.query.get(1)
	print(user_first1.name)

	# 条件
	user_filter = User.query.filter_by(name='Lsy').first()
	print(user_filter.name)

# test_add_user()
# test_query_user()