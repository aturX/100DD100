import json

def save(data, path):
	"""
    data 是 dict 或者 list
    path 是保存文件的路径
    """
	s = json.dumps(data, indent=2, ensure_ascii=False)
	with open(path, 'w+',encoding='utf-8') as f:
		f.write(s)

def load(path):
	with open(path, 'r', encoding='utf-8') as f:
		s = f.read()
		return json.loads(s)


class Model(object):
	@classmethod
	def db_path(cls):
		classname = cls.__name__
		path = 'data/{}.txt'.format(classname)
		return path

	@classmethod
	def all(cls):
		path = cls.db_path()
		models = load(path)
		ms = [cls.new(m) for m in models]
		return ms

	@classmethod
	def new(cls, form):
		m = cls(form)
		return m

	@classmethod
	def find_by(cls, **kwargs):
		k, v = '', ''
		for key, value in kwargs.items():
			k, v = key, value
		all = cls.all()
		for m in all:
			# getattr(m, k) 等价于 m.__dict__[k]
			if v == m.__dict__[k]:
				return m
		return None

	@classmethod
	def find_all(cls, **kwargs):
		"""
		用法如下，kwargs 是只有一个元素的 dict
		u = User.find_by(username='gua')
		"""

		k, v = '', ''
		for key, value in kwargs.items():
			k, v = key, value
		all = cls.all()
		data = []
		for m in all:
			# getattr(m, k) 等价于 m.__dict__[k]
			if v == m.__dict__[k]:
				data.append(m)
		return data

	def __repr__(self):
		"""
		__repr__ 是一个魔法方法
		简单来说, 它的作用是得到类的 字符串表达 形式
		比如 print(u) 实际上是 print(u.__repr__())
		"""
		classname = self.__class__.__name__
		properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
		s = '\n'.join(properties)
		return '< {}\n{} >\n'.format(classname, s)


	def save(self):
		"""
        用 all 方法读取文件中的所有 model 并生成一个 list
        把 self 添加进去并且保存进文件
        """
		models = self.all()
		first_index = 0
		if self.__dict__.get('id') is None:
			if len(models) > 3:
				self.id = models[-1].id + 1
			else:
				self.id = first_index
			models.append(self)
		else:
			index = -1
			for i, m in enumerate(models):
				if m.id == self.id:
					index = i
					break
				if index > -1:
					models[index] = self
		# 保存
		l = [m.__dict__ for m in models]
		path = self.db_path()
		save(l, path)


class User(Model):
	def __init__(self, form):
		self.id = form.get('id', None)
		if self.id is not None:
			self.id = int(self.id)
		self.username = form.get('username', '')
		self.password = form.get('password', '')

	def validate_login(self):
		# return self.username == 'gua' and self.password == '123'
		u = User.find_by(username=self.username)
		# us = User.all()
		# for u in us:
		#     if u.username == self.username and u.password == self.password:
		#         return True
		# return False
		return u is not None and u.password == self.password
		# 这样的代码是不好的，不应该用隐式转换
		# return u and u.password == self.password
	def validate_register(self):
		return len(self.username) > 2 and len(self.password) > 2


class Message(Model):
	"""
	Message 是用来保存留言的 model
	"""
	def __init__(self, form):
		self.author = form.get('author', '')
		self.message = form.get('message', '')

def test():
	form = dict(
		username='test',
		password='test01',
	)
	u = User(form)
	u.save()

if __name__ == '__main__':

	print(json.loads("[]"))

	# test()