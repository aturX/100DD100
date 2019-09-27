from UrlsList import User, db, Website

name = "Lsy"

websites = [
	{
		'name': '百度搜索',
		'url': 'http://www.baidu.com',
		'info': '搜索引擎'
	 },
	{
		'name': '多吉搜索',
		'url': 'https://www.dogedoge.com/',
		'info': '干净的搜索引擎'
	},
	{
		'name': '留言板项目',
		'url': 'http://sayhello.helloflask.com/',
		'info': '用Python + Flask 实现的留言板项目'
	},
	{
		'name': '电影列表项目',
		'url': 'http://watchlist.helloflask.com/',
		'info': '用Python + Flask 实现的电影信息展示列表项目'
	},
	{
		'name': 'Flask入门教程',
		'url': 'https://read.helloflask.com/',
		'info': 'Flask快速上手入门教程'
	},
	{
		'name': '狼牌导航站',
		'url': 'https://www.volf.club/',
		'info': '优秀的导航网站'
	},

]

# 全局的两个变量移动到这个函数内


def add_mock_data(name, websites):

	user = User(name=name)
	db.session.add(user)

	for website in websites:
		toadd_website = Website(name=website['name'], url=website['url'], info=website['info'])
		db.session.add(toadd_website)

	db.session.commit()

# add_mock_data(name, websites)

"""

$ flask shell
>>> from app import db
>>> db.create_all()
>>> db.drop_all()
>>> db.create_all()
"""

# 创建管理员用户
def admin(username, password):
	"""Create user."""
	db.create_all()

	user = User.query.first()
	if user is not None:
		user.username = username
		user.set_password(password)  # 设置密码
	else:
		user = User(username=username, name='Admin')
		user.set_password(password)  # 设置密码
		db.session.add(user)

	db.session.commit()  # 提交数据库会话


# db.drop_all()  # 清空旧表
# db.create_all()
# admin("admin", "admin")