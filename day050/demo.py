class Hello(object):

	def __init__(self, text):
		self.__text = text

	def say_hi(self):
		print(self.__text)


	def get_text(self):
		return self.__text

	def set_text(self, text):
		self.__text = text

	# 装饰器 ： 将方法当属性调用, 读数据
	@property
	def text(self):
		return self.__text

	# 装饰器 ： 将方法当属性调用, 写数据
	@text.setter
	def text(self, text):
		self.__text = text


h = Hello("hhhhh")

#print(h.text)
print(h.text)
h.text = "9999"

print(h.text)
print(h.get_text())