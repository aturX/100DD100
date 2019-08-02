# 可变参数就是传入的参数个数是可变的

def sum_a_b(a, b):
	return a + b

def sum_a_b_2(*ab):

	return ab

def sum_a_b_3(ab):
	return ab

# 1.可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 可变参数的使用意义
def main():
	a, b = 3, 5
	ab = [3, 5]
	c = sum_a_b(a, b)
	print(c)
	print(sum_a_b_2(ab, a, b))
	print(sum_a_b_3(ab))
	# print(sum_a_b_3(ab, a, b))  报错


def people(name, age, **kw):
	print(name, age, kw)

# 限定 关键字 参数名
def people2(name, age, *, city, job):
	print(name, age, city, job)

# 2. 关键字参数允许你传入0个或任意个"含参数名"（形参名）的参数，这些关键字参数在函数内部自动组装为一个dict
def main2():
	name = 'lsy'
	age = '25'
	print(people(name, age))
	print(people(name, age, city='shanghai'))
	c = dict(
		city='shanghai'
	)
#	print(people(name, age, c))  #报错
	people(name, age, other=c)
# 常用
	people(name, age, **c)

	people2(name, age, city='shanghai', job='it')
	# people2(name, age, city='shanghai', job2='it')   # 报错： 限定参数名
	# people2(name, age, **c)   # 报错： 限定参数名

# 任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
main2()

# *args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法