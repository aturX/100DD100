import sqlite3


# 建表 + 写数据
def write_one_line():
	conn = sqlite3.connect('test.db')

	cursor = conn.cursor()

	# 创建User 表
	cursor.execute('create table user2 (id varchar(20) primary key, name varchar(20))')

	# 插入 数据
	cursor.execute("insert into user (id, name) values ('1', 'lsy')")

	# 获得行数
	count = cursor.rowcount
	print("当前数据行{}".format(count))

	# 关闭Cursor
	cursor.close()

	# 提交事务
	conn.commit()

	# 关闭Connection
	conn.close()

# 查询 数据
def select_one():
	# 建立连接
	conn = sqlite3.connect('test.db')
	# 创建游标
	cursor = conn.cursor()
	# 执行查询语句
	cursor.execute("select * from user where id=?", (1,))
	# 查询到结果集
	values = cursor.fetchall()
	print("查询得到数据： {}".format(values))
	cursor.close()
	conn.close()

	# 使用Python的DB - API时，只要搞清楚Connection和Cursor对象