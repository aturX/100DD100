from UrlsList import db, User


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