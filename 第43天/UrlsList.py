"""
Flask 入门项目：
网站内容信息展示 UrlsList
参考：  http://watchlist.helloflask.com/
教程： https://read.helloflask.com/c1-ready

Done - 完成
- 完成  浏览器 编辑器 开发工具 ： Chrome  + Pycharm + Python3.7 + Flask + Pipenv + Git + Linux （Vim）
- 完成  配置虚拟环境 安装web框架  提交代码版本控制 ： Pipenv + Flask + GitHub
- 完成  配置Flask 的配置文件 .env .flaskenv  使用 python-dotenv


TODO - 待办
- 使用模板基础 ： 模板基本语法
- 编写主页模板
- 准备虚拟数据
- 渲染主页模板

"""

from flask import Flask, render_template

from mock import websites, name

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', name=name, websites=websites)



if __name__ == "__main__":
	app.run(host="0.0.0.0", port="6666")