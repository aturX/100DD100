# 一、 python 的函数可以传递
import datetime


def hello():
	a = 1
	b = 2
	print("hello {}".format(a+b))

def good():
	print("*"*10 + "Good!")

def log(func):
	# 函数 func.__name__ 可以得到函数名
	print("start: {}".format(func.__name__))
	func()
	print("end: {}".format(func.__name__))

log(hello)
log(good)

# 二、 装饰器： 语法糖，简化调用
# use_logging 就是一个装饰器，它一个普通的函数，它把执行真正业务逻辑的函数 func 包裹在其中，
# 看起来像 foo 被 use_logging 装饰了一样，use_logging 返回的也是一个函数，
# 这个函数的名字叫 wrapper。
# 在这个例子中，函数进入和退出时 ，被称为一个横切面，这种编程方式被称为面向切面的编程。


def log_start_end(func):
	# 这是一个装饰器
	def wrapper():
		print("start: {}".format(func.__name__))
		func()
		print("end: {}".format(func.__name__))

	return wrapper

def log_running(func):
	# 这是一个装饰器
	def wrapper():
		print("running: {}".format(func.__name__))
		return func()


	return wrapper

def new_hello():

	print("----------------new hellow world-----------------")

# 普通使用
new_hello = log_start_end(new_hello)
new_hello()

# 装饰器使用
# @ 符号就是装饰器的语法糖，它放在函数开始定义的地方，这样就可以省略最后一步再次赋值的操作
@log_start_end
def new2_hello():
	print("----------------new22222 hellow world-----------------")

new2_hello()

# 三、 作用： 可以轻松的拓展函数
@log_running
def new2_hello():
	print("----------------new22222 hellow world-----------------")

new2_hello()


# 四、 复杂场景： 传参函数
def log(func):
	def wrapper(*args, **kwargs):
		print(f"{datetime.datetime.today()} 模块： ", func.__name__)
		return func(*args, **kwargs)

	return wrapper

@log
def login():
	print(" User Login")

login()


# 五、 装饰器传参
# 装饰器本身需要传入参数，
# 那就需要编写一个返回装饰器函数的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log(text="用户退出模块")
def logout():
	print("User Logout")

logout()