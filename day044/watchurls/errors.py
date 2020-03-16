# 404 问题
from flask import render_template

from watchurls import app


@app.errorhandler(404)
def page_not_found(e):
	# user = User.query.first()  # 读取用户记录
	return render_template('errors/404.html'), 404  # 返回模板和状态码
