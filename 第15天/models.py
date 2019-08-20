from flask import json

from utils import log

# 写文件
def save(data, path):
	"""
	    本函数把一个 dict 或者 list 写入文件
	    data 是 dict 或者 list
	    path 是保存文件的路径
	    """
	# json 是一个序列化/反序列化(上课会讲这两个名词) list/dict 的库
	# indent 是缩进
	# ensure_ascii=False 用于保存中文
	s = json.dumps(data, indent=2, ensure_ascii=False)
	with open(path, "w+", encoding='utf-8') as f:
		log('save', data)
		f.write(s)

# 读文件
def load(path):
	with open(path, 'r', encoding='utf-8') as f:
		s = f.read()
		log("load", s)
		return json.loads(s)

# 数据存储的基类
class Model(object):
	# @classmethod 说明这是一个 类方法
	# 类方法的调用方式是  类名.类方法()
	@classmethod
	def db_path(cls):
		# classmethod 有一个参数是 class
		# 所以我们可以得到 class 的名字
		classname = cls.__name__
		path = 'db/{}.txt'.format(classname)
		return path

	@classmethod
	def new(cls, form):
		m = cls(form)
		return m

	@classmethod
	def find_by(cls, **kwargs):
		"""
		用法如下，kwargs 是只有一个元素的 dict
		u = User.find_by(username='gua')
		"""
		log('kwargs, ', kwargs)
		k, v = '', ''
		for key, value in kwargs.items():
			k, v = key, value
		all = cls.all()
		for m in all:
			if v == m.__dict__[k]:
				return m
		return None

	@classmethod
	def all(cls):
		"""
		得到一个类的所有存储的实例
		"""
		path = cls.db_path()
		models = load(path)
		ms = [cls.new(m) for m in models]
		log(ms)
		return ms

	def save(self):
		models = self.all()
		log('models', models)
		models.append(self)
		# __dict__ 是包含了对象所有属性和值的字典
		l = [m.__dict__ for m in models]
		path = self.db_path()
		log("l",l)
		save(l, path)

	def __repr__(self):
		"""
		这是一个 魔法函数
		类似java toString
		"""
		classname = self.__class__.__name__
		properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
		s = '\n'.join(properties)
		return '< {}\n{} >\n'.format(classname, s)


# 用户类
class User(Model):
	def __init__(self, form):
		self.username = form.get('username', '')
		self.password = form.get('password', '')

	def validate_login(self):
		# return self.username == 'gua' and self.password == '123'
		u = User.find_by(username=self.username)
		return u is not None and u.password == self.password

	def validate_register(self):
		return len(self.username) > 2 and len(self.password) > 2


# 消息类