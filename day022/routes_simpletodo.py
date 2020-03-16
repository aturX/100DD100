from utils import log
from utils import template

from models import Todo


def response_with_headers(headers, status_code=200):
    header = 'HTTP/1.1 {} OK\r\n'.format(status_code)
    header += ''.join(['{}: {}\r\n'.format(k, v)
                           for k, v in headers.items()])
    return header


def redirect(location):
    headers = {
        'Content-Type': 'text/html',
    }
    headers['Location'] = location
    # 302 状态码的含义, Location 的作用
    header = response_with_headers(headers, 302)
    r = header + '\r\n' + ''
    return r.encode(encoding='utf-8')


# 直接写函数名字不写 route 了
def index(request):
    """
    主页的处理函数, 返回主页的响应
    """
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    todo_list = Todo.all()
    body = template('simple_todo_index.html', todos=todo_list)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def add(request):
    """
    接受浏览器发过来的添加 todo 请求
    添加数据并发一个 302 定向给浏览器
    浏览器就会去请求 / 从而回到主页
    """
    # 得到浏览器发送的表单
    form = request.form()
    # 创建一个 todo
    Todo.new(form)
    # 让浏览器刷新页面到主页去
    return redirect('/')


def delete(request):
    """
    通过下面这样的链接来删除一个 todo
    /delete?id=1
    """
    todo_id = int(request.query.get('id'))
    Todo.delete(todo_id)
    return redirect('/')


route_dict = {
    '/': index,
    '/add': add,
    '/delete': delete,
}