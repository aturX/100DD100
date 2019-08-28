import pymongo
import random

# 连接数据库
client = pymongo.MongoClient("mongodb://localhost:27017")
print("连接数据库成功", client)
# 设置数据库
db_name = "test"   # 建库
# 使用
db = client[db_name]

# 插入数据
# ===
# mongo 中的 document 相当于 sqlite 中的 table
# 不需要定义，直接使用
# 不限定每条数据的字段
# 直接插入新数据，数据以字典的形式提供
# 下面的例子中， user 是文档名（表名），不存在的文档会自动创建
# 每个数据有一个自动创建的字段 _id，可以认为是 mongo 自动创建的主键

# 插入操作
def insert():
	user = {
		'name': 'sss',
		'age': '26',
		'id': random.randint(0, 100)
	}
	# 相当于 db['user'].insert
	db.user.insert(user)   # user 不存在会自动创建
	# db.event.insert(user)

# insert()

# 查找数据
def find():
	user_list = list(db.user.find())  #  查询所有内容 list 展示
	return user_list

# print(find())

# 条件查询
def find_one():
	query = {
		'age': '26',
	}
	user = list(db.user.find(query))

	print(user)
	query = {
		'随机值': {
			'$gt': 1
		},
	}
	print('random > 1', list(db.user.find(query)))
	#
	# $or 查询
	query = {
		'$or': [
			{
				'随机值': 2,
			},
			{
				'name': 'GUA'
			}
		]
	}
	# 可以灵活组合条件
# find_one()

# 更新数据
# ===
# 默认更新第一条查询到的数据
def update():
	query = {
		'随机值': 1,
	}
	form = {
		'$set': {
			'name': '更新 22222',
		}
	}
	options = {
		'multi': True,
	}
	# 注意, 上课这部分代码出问题了, 现在是修复过的
    # 相当于 db.user.update(query, form, multi=True)
	db.user.update(query, form, **options)


update()

# 如果想要更新所有查询到的数据
# 需要加入下面的参数 {'multi': True}
# db.user.update(query, form, {'multi': True})


# 删除
# ===
# 删除和 find 是一样的
# db.user.remove()

# all 是给用户使用的查询函数
def all():
	query = {
		'_deleted': False,
	}
	user_list = list(db.user.find(query))
	us = []
	for u in user_list:
		u.pop('_deleted')
		us.append(u)
	print('所有用户', len(us), us)