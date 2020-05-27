import sqlite3

from sqlalchemy.orm import sessionmaker


def sqlite3_demo():
	db_con = sqlite3.connect('demo.db')
	print(type(db_con))  # <class 'sqlite3.Connection'>

	sql = "select * from user"
	cur = db_con.execute(sql)
	print(type(cur))  # <class 'sqlite3.Cursor'>


def SQLAlchemy_demo():
	from sqlalchemy import create_engine
	# 创建引擎
	engine = create_engine("mysql+pymysql://lsy:006261@web4web.top:3306/lsy", max_overflow=5)
	# 执行sql语句
	result = engine.execute("select * from searcher_websites")
	res = result.fetchall()
	print(res)





from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
# ORM解决中文编码问题 sqlalchemy 默认使用latin-1进行编码。
# "mysql+pymysql://fuzj:123.com@127.0.0.1:3306/fuzj?charset=utf8"  encoding='utf-8'
engine = create_engine("mysql+pymysql://lsy:006261@web4web.top:3306/lsy", max_overflow=5,encoding='utf-8')

Base = declarative_base()
# 绑定数据库引擎
Session = sessionmaker(bind=engine)
session = Session()
class Webs(Base):
	__tablename__ = 'webs'
	id = Column(Integer, primary_key=True)    # 唯一编号
	name = Column(String(50), default='', unique=False)
	url = Column(String(50), default='', unique=True)
	cent = Column(Integer, default=0)

	def __str__(self):
		return (f'id={self.id}, name={self.name}, url={self.url} cent={self.cent} ')


def SQLAlchemy_ORM_dem(session):

	# 创建表
	# Base.metadata.create_all(engine)  # 创建表
	# Base.metadata.drop_all(engine)   #删除表
	obj = Webs(name="baidu5", url='http://www.baidu.com5')

	# 添加数据
	session.add(obj)
	session.commit()
	# 查询数据
	# session.query(Webs).filter(Webs.id > 2)
	q = session.query(Webs).all()
	for i in q:
		print(i)
# SQLAlchemy_demo()
SQLAlchemy_ORM_dem(session)