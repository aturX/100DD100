from flask import Flask, request, make_response, redirect, render_template, jsonify

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config['SECRET_KEY'] = 'hard to guess string'



@app.route('/')
def index():
	return render_template('index.html')

@app.route('/query')
def query_result():
	data = request.args.get("data")
	print("data: ", data)

	# 查询数据
	r = {
		"baidu": "bbb",
		"sougou": "ccc"
	}

	return jsonify(r)



@app.route('/search')
def search_page():
	#  搜索页面渲染
	return render_template('index.html')

@app.route('/result')
def result_page():
	#  查询结果页面渲染
	return render_template('result.html')



@app.route('/cookie')
def cookie():
	# 设置 cookie

	response = make_response('<h1>This document carries a cookie!</h1>')
	response.set_cookie('user', 'lsy')
	return response

@app.route('/redirect')
def redirect_page():
	# 重定向
	return redirect('http://lisiyi.top')

@app.route('/result/<result>')
def args_page(result):
	# query 地址传参
	response = make_response('<h1>This document carries a cookie!,{}</h1>'.format(result))
	response.set_cookie('user', result)
	return response


@app.route('/home/<home>')
def home_page(home):
	return '<h1>Home Page</h1>'



if __name__ == '__main__':
	app.run(debug=True)