from jinja2 import Environment, FileSystemLoader
import os.path
import time

def log(*args, **kwargs):
    # time.time() 返回 unix time
    # 如何把 unix time 转换为普通人类可以看懂的格式呢？
    format = '%Y-%m-%d %H:%M:%S -----'   # 最常用的时间格式
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    print(dt, *args, **kwargs)
    with open('log.demo.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, **kwargs, file=f)  # 写入到文件


# Jinja2 模板渲染  本节重点
def template(path, **kwargs):
    """
    本函数接受一个路径和一系列参数
    读取模板并渲染返回
    """
    t = env.get_template(path)
    return t.render(**kwargs)



print(__file__)
log('test')
# __file__ 就是本文件的名字
# 得到用于加载模板的目录
path = '{}/templates/'.format(os.path.dirname(__file__))

# 创建一个加载器, jinja2 会从这个目录中加载模板
loader = FileSystemLoader(path)

# 用加载器创建一个环境, 有了它才能读取模板文件
env = Environment(loader=loader)


if __name__ == '__main__':
    # 模板渲染页面
    template('index.html')