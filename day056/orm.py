
'''
Python 中可以使用metaclass （元类）进行创建class。
简单的解释就是：
- 定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
- metaclass(元类)以后，就可以根据这个元类创建出类，所以：先定义metaclass，然后创建类。

创建顺序是：先定义metaclass，就可以创建类，最后创建实例。


要编写一个ORM框架，所有的类都只能动态定义，
因为只有使用者才能根据表的结构定义出对应的类来。
'''

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