from routes import template, response_with_headers, redirect
from todo import Todo

def index(request):
	"""
	   todo 首页的路由函数
	   """
	headers = {
		'Content-Type': 'text/html',
	}
	todo_list = Todo.all()
	# 下面这行生成一个 html 字符串
	todo_html = ''.join(['<h3>{} : {}</h3>'.format(t.id, t.title) for t in todo_list])
	# 替换模板文件中的标记字符串
	body = template('todo_index.html')
	body = body.replace('{{todos}}', todo_html)
	header = response_with_headers(headers)
	r = header + '\r\n' + body
	return r.encode(encoding='utf-8')


def add(request):
	"""
	用于增加新 todo 的路由函数
	"""
	headers = {
		'Content-Type': 'text/html',
	}
	if request.method == 'POST':
		form = request.form()
		t = Todo.new(form)
		t.save()
	# 浏览器发送数据过来被处理后, 重定向到首页
	# 浏览器在请求新首页的时候, 就能看到新增的数据了
	return redirect('/todo')


todo_route = {
    '/todo': index,
    '/todo/add': add,
}
