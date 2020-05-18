# Python面向对象编程：实现IoC控制反转


## 面向对象基础知识

1. `type()` 判断数据类型
2. `isinstance(a,b)` 判断class继承关系
3. `dir()` 获取相关属性
4. `__slots__`
   限制属性添加,class类可以任意添加属性，`__slots__`用于限制添加的属性
5. `@property` 和 `@x.setter` 装饰器，主要功能是：把一个方法变成属性调用
   解决的问题是，对于数据的检验，类似Java中的get
   set方法，但是可以对属性进行必要的检验，而对外暴露的依然是对属性的操作
   ```
   class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
        
   使用：
   
    >>> s = Student()
    >>> s.score = 60 # OK，实际转化为s.set_score(60)
    >>> s.score # OK，实际转化为s.get_score()
    60
    >>> s.score = 9999
    Traceback (most recent call last):
      ...
    ValueError: score must between 0 ~ 100!
   ```
6. 枚举类型:
   枚举类型可以当普通常量来使用，而且这些常量属同一类，比如星期，月份，错误编码，控制代码等。
   
   ```
   from enum import Enum
   # 固定 定值 采用枚举
    class MaxCent(Enum):
        People = 30
        Air = 30
        Place = 20
        Other = 20

    print(MaxCent["People"])
    ```


## 面向对象编程实践 

IoC 解决的核心问题是： 
- 谁负责创建组件？ 
- 谁负责根据依赖关系组装组件？
- 销毁时，如何按依赖顺序正确销毁？ 

--- 

1. 传统的应用程序中，控制权在程序本身，程序的控制流程完全由开发者控制

例：
```
class DB():	
    def __init__(self, config):	
        print("使用{}进行数据库连接操作".format(config))

	def query(self, data):
		print("查询: {}".format(data))

	def delete(self, data):
		print("删除： {}".format(data))
		
class Config():
    def __init__(self):
        print("配置信息")

class QueryService():
    def __init__(self):
        print("控制程序，顺序执行，创建对象")
        config = Config()
        db = DB(config)
    
        db.query("test query")

class DeleteService():
    def __init__(self):
        print("同上, Config 和 DB 再次被实例化")
        config = Config()
        db = DB(config)
        db.delete("test delete")


QueryService()
DeleteService()
```

2. 在IoC模式下，控制权发生了反转，即从应用程序转移到了IoC容器，所有组件不再由应用程序自己创建和配置，而是由IoC容器负责
，这样，应用程序只需要直接使用已经创建好并且配置好的组件。为了能让组件在IoC容器中被“装配”出来，需要某种“注入”机制
比如，上方： DB 将不再由 QueryService， DeleteService
自己创建，而是等待外部，通过“方法”注入 比如交由一个 setDB()

例： 
``` 
class QueryServiceIoC():

	def __init__(self):
		self.db = None
	# 依赖注入（DI：Dependency Injection）
	def setDB(self, db):
		self.db = db

	def query(self):
		print("通过注入查询")
		self.db.query("test IoC Query")

class DeleteServiceIoC():

	def __init__(self):
		self.db = None

	def setDB(self, db):
		self.db = db

	def delete(self):
		self.db.delete("test IoC Delete")
```


IoC又称为依赖注入（DI：Dependency
Injection），它解决了一个最主要的问题：将组件的创建+配置与组件的使用相分离，并且，由IoC容器负责管理组件的生命周期。
(参考 Java
Spring)因为IoC容器要负责实例化所有的组件，因此，有必要告诉容器如何创建组件，以及各组件的依赖关系。
一种最简单的配置是通过XML文件来实现

```
 <beans> <bean id="DB" class="DB" />
    
    <bean id="QueryServiceIoC" class="QueryServiceIoC">
        <property name="DB" ref="DB" />
    </bean>
    
    <bean id="DeleteServiceIoC" class="DeleteServiceIoC">
        <property name="DB" ref="DB" />
    </bean>
</beans>
分别三个 Bean 组件， DB 被分别注入到  QueryServiceIoC 和 DeleteServiceIoC 中
```

除了 set() 方法可以注入，还可以直接构造方法/初始化注入 

``` 
class QueryServiceIoCNew():	
    # 依赖注入（DI：Dependency Injection）	
    def __init__(self, db):	self.db = db

    def query(self):
        print("通过注入查询")
        self.db.query("test IoC Query")
```
Java Spring的IoC容器同时支持属性注入和构造方法注入，并允许混合使用
 
Python 实现 IoC 思路， 由于Spring 使用 XML 存储 Bean 组件的依赖关系，在Python中实现则用一个BeanFactory替代，
context: 存储Bean的名字和对应的类或者值的字典 
allowRepalce: 是否允许替换已经注入的Bean
 
```
# 依赖管理
class BeanFactory():
	def __init__(self,allowReplace=False):
		"""构造函数 allowReplace:是否允许替换已经注入的bean """
		self.context = {}
		self.allowReplace = allowReplace

	def setBean(self, beanName, resource, *args, **kwargs):
		if not self.allowReplace:
			assert not beanName in self.context, "该BeanFactory不允许重复注入%r,请修改beanName" % beanName

		# 闭包函数
		def call():
			"""定义一个函数闭包,如果注入的resource是可调用类型,
			就将*args和**kwargs传入并调用该函数,然后将返回值返回
			如果是一个不可调用对象,就直接返回 """
			if callable(resource):
				return resource(*args, **kwargs)
			else:
				return resource

		# 将call闭包与beanName建立映射
		self.context[beanName] = call


	def __getitem__(self, beanName):
		"""重载__getitem__方法,使得BeanFactory支持使用[]获取beanName对应的注册的资源 """
		try:
			# 从context字典中取出beanName对应的资源
			resource = self.context[beanName]
		except KeyError:
			raise KeyError("%r 未注册" % beanName)
		# 返回闭包函数调用后的结果
		return resource()

SpringIoCFactory = BeanFactory()



def HasMethods(*methods):
	def test(obj):
		for each in methods:
			try:
				attr = getattr(obj, each)
			except AttributeError:
				return False
			if not callable(attr): return False
		return True
	return test

def NoAssertion(obj): return True
class RequiredResource(object):
	def __init__(self, beanName, assertion=NoAssertion):
		self.beanName = beanName
		self.assertion = assertion
	def __get__(self, obj, T):#每次访问descriptor时都会调用__get__方法
		return self.result # <-- .操作符会自动调用__getattr__
	def __getattr__(self, name):
		assert name == 'result', "Unexpected attribute request other then 'result'"
		self.result = self.Request()
		return self.result
	def Request(self):
		obj = SpringIoCFactory[self.beanName]
		assert self.assertion(obj), \
			"The value %r of %r does not match the specified criteria" \
			% (obj, self.feature)
		return obj



class TestIoCService():
	# 依赖注入（DI：Dependency Injection）
	db = RequiredResource('db')
	def __init__(self):
		self.s = "初始化成功， 注入 db:  "

	def print_db_info(self):
		self.db.query("通过依赖注入进行的查询！")


class DB_IoC():
	# 依赖注入（DI：Dependency Injection）
	config = RequiredResource('config')
	def __init__(self):
		print("使用{} 进行数据库连接操作".format(self.config))

	def query(self, data):
		print("查询: {}".format(data))

	def delete(self, data):
		print("删除： {}".format(data))


if __name__ == "__main__":
	print("******* Test IoC Demo ********")
	SpringIoCFactory.setBean("db", DB_IoC)
	SpringIoCFactory.setBean("config", Config)

	# 测试
	tic = TestIoCService()
	tic.print_db_info()

	"""
	实现了 DB类 和Config 类 ，通过 IoC 方式进行依赖注入
	BeanFactory 是一个简易的IoC管理器，然后通过 RequiredResource 将需要实例化的类
	注入到使用的类中，完成“依赖注入”。
	而DB类 和Config类的实例化过程，并不是使用时才被实例化，而是提前被IoC容器创建，在使用的时候
	只是直接获取。从而实现“控制反转”
	"""
```	
	
	
# 参考资料
- [面对对象高级编程](https://www.liaoxuefeng.com/wiki/1016959663602400/1017502538658208)

- [Python IoC 实现](http://www.voidcn.com/article/p-vxpqmayc-brn.html)