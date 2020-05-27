# Python 元类及ORM框架实现


## Python 数据库操作

数据库操作的基本过程：

1. 要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection
```
# 用 Python 的 sqlite 数据库举例

import sqlite3   

# 连接数据库，获得Connection
db_con = sqlite3.connect('demo.db')

print(type(db_con))  # <class 'sqlite3.Connection'>
```

2. 连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果
```
sql = "select * from user"
cur = db_con.execute(sql)
print(type(cur))    # <class 'sqlite3.Cursor'>
```
3. 在Python中操作数据库时，要先导入数据库对应的**驱动**，然后，通过Connection对象和Cursor对象操作数据
```
import sqlite3    # 数据库驱动
```


## 对象关系映射（Object-Relational Mapper，ORM）

ORM 是一个数据抽象层，在ORM的概念中，类对应数据库中的表，属性对应列，
类的单个实例表示数据库中的一行数据。 Python 编程语言常用的ORM
框架是SQLAlchemy。，该框架建立在数据库API之上，使用关系对象映射进行数据库操作，
简言之便是：将对象转换成SQL，然后使用数据库API执行SQL并获取执行结果。
SQLAlchemy本身无法操作数据库，其必须以来pymsql等第三方插件，Dialect用于和数据API进行交流，
根据配置文件的不同调用不同的数据库API，从而实现对数据库的操作。

```
MySQL-Python
    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
  
pymysql
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
  
MySQL-Connector
    mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
  
cx_Oracle
    oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]
  
更多详见：http://docs.sqlalchemy.org/en/latest/dialects/index.html
```

- SQLAlchemy 底层处理
使用 Engine/ConnectionPooling/Dialect 进行数据库操作，Engine使用ConnectionPooling连接数据库，然后再通过Dialect执行SQL语句。

```
def SQLAlchemy_demo():
	from sqlalchemy import create_engine
	import sqlalchemy
	import pymysql
	# 创建引擎
	engine = create_engine("mysql+pymysql://xxxxx:xxxxx@127.0.0.1:3306/mysql", max_overflow=5)
	# 执行sql语句
	result = engine.execute("select * from searcher_websites")
	res = result.fetchall()
	print(res)
```

- ORM 功能

ORM 映射对象，完成建表，查询等，操作数据库方式
```

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
# ORM解决中文编码问题 sqlalchemy 默认使用latin-1进行编码。
  
engine = create_engine("mysql+pymysql://user:password@127.0.0.1:3306/mysql?charset=utf8", max_overflow=5,encoding='utf-8')
Base = declarative_base()

# 绑定数据库引擎
Session = sessionmaker(bind=engine)
session = Session()


# 创建于表映射的 实体类
class Webs(Base):
	__tablename__ = 'webs'
	id = Column(Integer, primary_key=True)    # 唯一编号
	name = Column(String(50), default='', unique=False)
	url = Column(String(50), default='', unique=True)
	cent = Column(Integer, default=0)
    
    # 打印内容
	def __str__(self):
		return (f'id={self.id}, name={self.name}, url={self.url} cent={self.cent} ')


def SQLAlchemy_ORM_demo(session):

	# 创建表
	Base.metadata.create_all(engine)  # 创建表
	# Base.metadata.drop_all(engine)   #删除表
	obj = Webs(name="baidu", url='http://www.baidu.com')

	# 添加数据
	session.add(obj)
	session.commit()
	# 查询 / 条件查询数据
	# session.query(Webs).filter(Webs.id > 2)
	q = session.query(Webs).all()
	for i in q:
		print(i)

SQLAlchemy_ORM_dem(session)
```

## ORM 框架实现

Python 中可以使用metaclass （元类）进行创建class。
简单的解释就是：
- 定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

- metaclass(元类)以后，就可以根据这个元类创建出类，所以：先定义metaclass，然后创建类。
创建顺序是：先定义metaclass，就可以创建类，最后创建实例。
要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

如上章所示，使用ORM框架提供的`Column`类或者'Field'类来对应数据库的表字段。

首先来定义`Field`类，它负责保存数据库表的字段名和字段类型：

```
# Field 类 它负责保存数据库表的字段名和字段类型：
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
        self.default = None  # 字段默认值

    def __str__(self):
        return f'{self.__class__.__name__}:{self.name}'


# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField
class StringField(Field):
    # 实现 varchar 类型
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(256)')

class IntegerField(Field):
    # 实现 int 类型
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

# 编写 metaclass 类, 元类继承 type
class ModelMetaclass(type):
    # name 名字  bases  继承父类   attrs 继承属性
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        # 重点理解： 不同的表 字段不同，添加的 方法 属性 也不同
        mappings = dict()
        for k, v in attrs.items():
            # 在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v


        for k in mappings.keys():
            # 从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

# 创建 基类
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        for k, v in self.__mappings__.items():
            # 更加字段 建立映射  不满足条件的不映射
            fields.append(v.name)
            params.append(getattr(self, k, v.default))

        sql = f'''insert into {self.__table__} ({",".join(fields)}) values ('{"','".join(params)}')'''
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(params))


# 使用 ORM
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id='0000', name='admin', email='test@gmail.com', password='admin')
# 保存到数据库：
u.save()

# 实现效果： ORM框架就是将实体类映射成可执行的SQL操作数据库
```




## 参考

- [使用Python ORM框架](https://www.cnblogs.com/pycode/p/mysql-orm.html)

- [实现Python ORM框架](https://www.liaoxuefeng.com/wiki/1016959663602400/1018490605531840)
 
- [Djang ORM 源码分析](https://zhuanlan.zhihu.com/p/35746049)

























