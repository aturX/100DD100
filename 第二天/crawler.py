import socket
import ssl

def log(*args, **kwargs):
    print("Log: ", *args, **kwargs)


def parsed_url(url):
    """
    解析 url 返回 (protocol host port path)
    有的时候有的函数, 它本身就美不起来, 你要做的就是老老实实写
    """
    # 检查协议
    protocol = 'http'
    if url[:7] == 'http://':
        u = url.split('://')[1]
    elif url[:8] == 'https://':
        protocol = 'https'
        u = url.split('://')[1]
    else:
        # '://' 定位 然后取第一个 / 的位置来切片
        u = url

    # 检查默认 path
    i = u.find('/')
    if i == -1:
        host = u
        path = '/'
    else:
        host = u[:i]
        path = u[i:]

    # 检查端口
    port_dict = {
        'http': 80,
        'https': 443,
    }
    # 默认端口
    port = port_dict[protocol]
    if host.find(':') != -1:
        h = host.split(':')
        host = h[0]
        port = int(h[1])

    return protocol, host, port, path


#  请求
def path_with_query(path, query):
    '''
    path 是一个字符串
    query 是一个字典

    返回一个拼接后的 url
    详情请看下方测试函数
    '''
    p = "?"
    for key, value in query.items():
        p += str(key) + "=" + str(value) + "&"
    p = path + p[:-1]  # 去掉最后一个&
    return p


def test_path_with_query():
    # 注意 height 是一个数字
    path = '/'
    query = {
        'name': 'gua',
        'height': 169,
    }
    expected = [
        '/?name=gua&height=169',
        '/?height=169&name=gua',
    ]
    # NOTE, 字典是无序的, 不知道哪个参数在前面, 所以这样测试
    assert path_with_query(path, query) in expected


# 解析请求头
def header_from_dict(headers):
    '''
    headers 是一个字典
    范例如下
    对于
    {
    	'Content-Type': 'text/html',
        'Content-Length': 127,
    }
    返回如下 str
    'Content-Type: text/html\r\nContent-Length: 127\r\n'
    '''
    q = ""
    for key, value in headers.items():
        q += key + ": " + value + "\r\n"

    return q


def test_header_from_dict():
    """
   host: cn.bing.com
   accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
   accept-encoding: gzip, deflate, br
   accept-language: zh-CN,zh;q=0.9,en;q=0.8


   """
    headers_items = {
        'authority': 'cn.bing.com',
        'Content-Type': 'text/html',
    }

    excepted = "authority: cn.bing.com\r\nContent-Type: text/html\r\n"
    output_query = header_from_dict(headers_items)

    e = "测试不通过:\r\n {} != {}".format(excepted, output_query)
    assert output_query == excepted, e

# https 或 HTTP socket返回
def socket_by_protocol(protocol):

    if protocol == 'http':
        s = socket.socket()
    else:
        # HTTPS 协议需要使用 ssl.wrap_socket 包装一下原始的 socket
        # 除此之外无其他差别
        s = ssl.wrap_socket(socket.socket())
    return s


# 获取响应
def response_by_socket(s):
    buffer_size = 1024
    response = b''
    while True:
        r = s.recv(buffer_size)
        response += r
        if len(r) == 0:
            break
    return response


def parsed_response(r):
	"""
    把 response 解析出 状态码 headers body 返回
    状态码是 int
    headers 是 dict
    body 是 str
    """
	header, body = r.split('\r\n\r\n', 1)
	h = header.split('\r\n')
	status_code = h[0].split()[1]
	status_code = int(status_code)

	headers = {}
	for line in h[1:]:
		k, v = line.split(': ')
		headers[k] = v
	return status_code, headers, body

def get(url, query):
    """
    本函数使用上课代码 client.py 中的方式使用 socket 连接服务器
    获取服务器返回的数据并返回
    注意, 返回的数据类型为 bytes
    完成一个简单的浏览器(客户端) ， 类似Chrome : 其功能， (1)访问网站，(2)获得内容，(3)展示出来
    我们的目的是： 访问别人的服务器。 就像我们用Chrome访问百度，访问知乎 一样.
    """
    protocol, host, port, path = parsed_url(url)
    log("访问：", protocol, host, port, path)

    s = socket_by_protocol(protocol)
    s.connect((host, port))  # 连接网络： 访问网站

    headers = header_from_dict(query)
    http_request = 'GET {} HTTP/1.1\r\nhost: {}\r\nConnection: close\r\n{}\r\n'.format(path, host, headers)
    request = http_request.encode("utf-8")
    log("***用户开始访问: {}".format(url))
    log("***用户发送请求: [{}]".format(request))

    s.send(request)

    response = response_by_socket(s)
    r = response.decode("utf-8")
    # log("响应", r)
    status_code, headers, body = parsed_response(r)
    if status_code in [301, 302]:
        url = headers['Location']
        return get(url, query)
    return status_code, headers, body


if __name__ == "__main__":
    # test_path_with_query()
    url = 'https://movie.douban.com/top250'
    query = {
        'Accept': 'text/html',
        'Accept - Language': 'zh - CN, zh;q = 0.9, en;q = 0.8',
    }
    get(url, query)





