

# 框架Request 对象,保存请求数据
import socket
import logging
import urllib.parse

from routes import route_static, route_dict
from routes_todo import todo_route


class Request(object):
    def __init__(self):
        self.method = 'GET'
        self.path = ''
        self.query = {}
        self.body = ''
        self.headers = {}
        self.cookies = {}

    def form(self):
        '''
        a=123&b=456
        :return:    {a:123,b:456}
        '''
        body = urllib.parse.unquote(self.body)
        args = body.split('&')
        f = {}
        for arg in args:
            k, v = arg.split('=')
            f[k] = v

        return f

    def add_cookies(self):
        '''
        user=123;pwd=456
        :return:
        '''
        cookies = self.headers.get('Cookie', '')  # 有则取， 无则空
        kvs = cookies.split('; ')
        for kv in kvs:
            if '=' in kv:
                k, v = kv.split('=')
                self.cookies[k] = v

    def add_headers(self, header):
        '''
        aaa: 111,
        bbb: 222,
        ccc: 333,
        :return:
        '''
        lines = header
        for line in lines:
            k, v = line.split(': ', 1)
            self.headers[k] = v

        # 添加完头部之后， 就有了Cookies 的信息
        self.cookies = {}   # 清除cookies
        self.add_cookies()


def error(request, code=404):
    """
    根据 code 返回不同的错误响应
    目前只有 404
    """
    # 之前上课我说过不要用数字来作为字典的 key
    # 但是在 HTTP 协议中 code 都是数字似乎更方便所以打破了这个原则
    e = {
        404: b'HTTP/1.x 404 NOT FOUND\r\n\r\n<h1>NOT FOUND</h1>',
    }
    return e.get(code, b'')


# 解析path 路径 和 query     http:localhost:8080/path/?a=123&b=456 --> path   {a: 123, b: 456}
def parsed_path(path):
    index = path.find('?')
    if index == -1:  # 没有query
        return path, {}
    else:
        path, query_string = path.split('?', 1)
        args = query_string.split('&')
        query = {}
        for arg in args:
            k, v = arg.split('=')
            query[k] = v
        return path, query

# 解析path 获取响应
def response_for_path(path):
    path, query = parsed_path(path)
    request.path = path
    request.query = query
    r = {
        '/static': route_static,
    }
    r.update(route_dict)
    r.update(todo_route)
    response = r.get(path, error)
    return response(request)


# 主程序运行
def run(host='', port=5000):
    '''
    启动服务器
    '''
    print("启动服务器")
    with socket.socket() as s:
        s.bind((host, port))
        while True:
            print("开始监听...")
            s.listen(3)
            connection, address = s.accept()
            print(address)
            r = connection.recv(1000)
            r = r.decode('utf-8')

            logging.info("ip :{} ".format(address))
            logging.info("request :{} ".format(r))
            if len(r.split()) < 2:
                continue

            path = r.split()[1]
            # 设置 request 的 method
            request.method = r.split()[0]
            request.add_headers(r.split('\r\n\r\n', 1)[0].split('\r\n')[1:])
            request.body = r.split('\r\n\r\n', 1)[1]
            # 用 response_for_path 函数来得到 path 对应的响应内容
            response = response_for_path(path)
            logging.info('debug **', 'sendall')
            # 把响应发送给客户端
            connection.sendall(response)
            # 处理完请求, 关闭连接
            connection.close()


request = Request()

if __name__ == '__main__':

    config = dict(
        host='localhost',
        port=4444
    )
    run(**config)