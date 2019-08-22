import random

from flasgger import Swagger
from flask import Flask, request, jsonify

app = Flask(__name__)
Swagger(app)

# Todo 访问API 接口地址 ： http://localhost:5000/apidocs/
# 使用Restful API 风格


"""
分清楚HTTP请求中：
1. path    /path  
2. query   ?a=123&b=456
3. body    不存在路径中，存在请求体中  ?a=123&b=456
"""


@app.route('/api/<string:language>/', methods=['GET'])
def index(language):
	"""
    API接口文档 演示接口
    调用这个接口，输入一种语言的名字，查看具体的语言特性
    ---
    tags:
      - 演示Swagger API
    parameters:
      - name: language
        in: path
        type: string
        required: true
        description: 输入语言 ，如Python， 提交数据在Path中
        value: python
      - name: size
        in: query
        type: integer
        description:  展示内容的数量， 提交数据存在Request query中
        value: 1
    responses:
      500:
        description: 服务器报错
      200:
        description: 200 OK
        schema:
          properties:
            language:
              type: string
              description: The language name
              default: Lua
            features:
              type: array
              description: The awesomeness list
              items:
                type: string
              default: ["test1", "test2", "test2"]

    """

	language = language.lower().strip()
	features = [
		"awesome", "great", "dynamic",
		"simple", "powerful", "amazing",
		"perfect", "beauty", "lovely"
	]
	size = int(request.args.get('size', 1))
	if language in ['php', 'vb', 'visualbasic', 'actionscript']:
		return "An error occurred, invalid language for awesomeness", 500
	return jsonify(
		language=language,
		features=random.sample(features, size)
	)


@app.route('/test/<string:username>/', methods=['GET'])
def say_hello(username):
	"""
	演示say_hello
	---
	    tags:
	      - 测试 API
	    parameters:
	      - name: username
	        in: path
	        type: string
	        required: true
	        description: 输入用户名
	        value: lsy
	    responses:
	      200:
	        schema:
	          properties:
	            content:
	              type: string
	              description: 打印字符串 hello lsy
	              default: hello lsy
	    """
	return jsonify(
		content="Hello  " + username
	)


app.run(debug=True)
