'''
Python有一些高阶函数，能够非常容易的解决一些比较特殊的场景问题。常用的几个函数如下所示。

1. map
场景一：
```
有一批值或者数据，需要重复的执行同一个逻辑过程。用map函数把list中所有数字转为字符串：
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
['1', '2', '3', '4', '5', '6', '7', '8', '9']

实例场景：有一批用户名数据，现要求根据用户名，生成随机密码，给每个用户分配一个密码。
```
'''


# user = ["xxxx",""]
def gen_password(user):
    from random import randint
    # 生成随机密码
    str_password = ""
    str_str = "abcdefghij"
    for i in range(8):
        num = randint(0, 9)
        str_password = str_password + str_str[num]

    password = str_password + user[0] + str_password    # 用用户名拼接一个密码
    user[1] = password
    print("用户生成的随机信息是: {}".format(user))
    return user

def demo1():
    # 场景一： 密码生成
    users_data = [
        ["admin", ""],
        ["userone", ""],
        ["aturx", ""],
        ["lisiyi", ""],
        ["whoareyou", ""]
    ]

    result = map(gen_password, users_data)
    print(list(result))


#demo1()

'''
2. reduce
场景二：
```
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做计算，其效果就是：

reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

实例场景：现有一个软件系统一年内每个月利润值，想要统计全年总利润。
```
'''




def new_add_user(before, now):
    new_add = now + before
    return new_add


def demo2():
    # 场景二： 累计统计
    data = [
        1000, 1300, 1500, 4572,
        1976, 2230, 1212, 2222,
        1567, 2621, 3000, 2320
    ]
    from functools import reduce
    all = reduce(new_add_user, data)

    print(all)

#demo2()

'''
3. filter
场景三：
```
Python内建的filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。


实例场景：某系统有大量注册用户，先需要在一批注册用户中，找到年龄为40岁以上的男性用户。该场景非常适合使用过滤器。
```
'''


def is_man(user):
    # 过滤40岁以上男性
    if user[0] == "man" and user[1] > 40:
        return True
    else:
        return False

def demo3():
    # 场景三： 过滤特定数据
    data = [
        ["man", 30],
        ["woman", 22],
        ["woman", 22],
        ["man", 42],
        ["woman", 22],
        ["man", 52],
        ["woman", 22],
        ["man", 12],
        ["woman", 62],
        ["man", 48],
        ["man", 62],
        ["woman", 22],
        ["man", 39],
        ["woman", 22],
    ]
    result_data = filter(is_man, data)
    print(list(result_data))

#demo3()

'''
4. sorted
场景四：
```
排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。

sorted()函数是一个高阶函数，它还可以接收一个key函数来实现自定义的排序。

实例场景： 现有一个班级学生的考试成绩单，先需要分别根据数学成绩排名（100分制）、英语成绩（ABCD制）排名。该场景适合自定义排序。
```
'''
def get_m_sort(student):
    # 返回数学分值
    return student[1]

def get_e_sort(student):
    # 返回英语分值
    return student[2]

def sorted_by_math(students):
    result = sorted(students, key=get_m_sort, reverse=True)  # 数字降序排列
    return result

def sorted_by_english(students):
    result = sorted(students, key=get_e_sort)
    return  result

def demo4():
    # 名字， 数学成绩， 英语成绩
    students = [
        ["people1", 99, "C"],
        ["people2", 78, "B"],
        ["people3", 85, "B"],
        ["people4", 63, "F"],
        ["people5", 79, "C"],
        ["people6", 68, "D"],
        ["people7", 53, "A"],
    ]

    order_by_math = sorted_by_math(students)

    order_by_english = sorted_by_english(students)

    print("数学排名: ", order_by_math)
    print("*" * 10)
    print("英语排名: ", order_by_english)

#demo4()







