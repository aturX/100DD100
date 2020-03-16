from jinja2 import Environment, FileSystemLoader
import os.path


# __file__ 就是本文件的名字
# 得到用于加载模板的目录
path = '{}/templates/'.format(os.path.dirname(__file__))
# 创建一个加载器, jinja2 会从这个目录中加载模板
loader = FileSystemLoader(path)
# 用加载器创建一个环境, 有了它才能读取模板文件
env = Environment(loader=loader)

# 调用 get_template() 方法加载模板并返回
template = env.get_template('index.html')

# 用 render() 方法渲染模板
# 可以传递参数
ns = list(range(3))
us = [
    {
        'id': 1,
        'name': '李思毅',
    },
    {
        'id': 2,
        'name': '房檐',
    },
]
print(template.render(name='lsy', numbers=ns, users=us))
