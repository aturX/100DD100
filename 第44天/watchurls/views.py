from flask import request, url_for, flash, render_template
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.utils import redirect
from watchurls import app, Website, db, User


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	# 读取数据库
	if request.method == 'POST':  # 判断是否是 POST 请求
		if not current_user.is_authenticated:  # 如果当前用户未认证
			return redirect(url_for('index'))  # 重定向到主页
		name = request.form.get('name')
		url = request.form.get('url')
		# 验证数据
		if len(name) < 1 or len(url) < 1:
			flash('信息填写错误！')  # 显示错误提示
			return redirect(url_for('index'))  # 重定向回主页
		# 保存表单数据到数据库
		website = Website(name=name, url=url)  # 创建记录
		db.session.add(website)  # 添加到数据库会话
		db.session.commit()  # 提交数据库会话
		flash('网址添加成功！')  # 显示成功创建的提示
		return redirect(url_for('index'))  # 重定向回主页
	# name = User.query.first().name  # 读取用户记录
	websites = Website.query.all()  # 查询全部网站数据
	return render_template('index.html', websites=websites)


# 在子模板里，我们可以使用 extends 标签来声明继承自某个基模板

# 编辑网站内容
@app.route('/website/edit/<int:website_id>', methods=['GET', 'POST'])
@login_required  # 登录保护
def edit(website_id):
	website = Website.query.get_or_404(website_id)
	# GET 和 POST 在同一路由中使用
	if request.method == 'POST':  # 处理编辑表单的提交请求
		name = request.form['name']
		url = request.form['url']
		if len(name) < 1 or len(url) < 1:
			flash('信息填写错误！')
			return redirect(url_for('edit', website_id=website_id))  # 重定向回对应的编辑页面

		website.name = name  # 更新名称
		website.url = url  # 更新网址
		db.session.commit()  # 提交数据库会话
		flash('修改成功！')
		return redirect(url_for('index'))  # 重定向回主页

	return render_template('edit.html', website=website)  # 传入被编辑的电影记录


@app.route('/website/delete/<int:website_id>', methods=['POST'])
@login_required  # 登录保护
def delete(website_id):
	movie = Website.query.get_or_404(website_id)  # 获取记录
	db.session.delete(movie)  # 删除对应的记录
	db.session.commit()  # 提交数据库会话
	flash('删除成功！')
	return redirect(url_for('index'))  # 重定向回主页



# --------------------------  Login  ---------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		if not username or not password:
			flash('输入错误！')
			return redirect(url_for('login'))

		user = User.query.first()
		# 验证用户名和密码是否一致
		if username == user.username and user.validate_password(password):
			login_user(user)  # 登入用户  (Flask-login的插件)
			flash('登录成功！')
			return redirect(url_for('index'))  # 重定向到主页
		flash('输入用户名或密码错误！')  # 如果验证失败，显示错误消息
		return redirect(url_for('login'))  # 重定向回登录页面

	return render_template('login.html')

# -------------------------- Logout ----------------------------------
@app.route('/logout')
@login_required  # 用于视图保护，后面会详细介绍
def logout():
	logout_user()  # 登出用户
	flash('已退出！')
	return redirect(url_for('index'))  # 重定向回首页

# 对于不允许未登录用户访问的视图，只需要为视图函数附加一个 login_required 装饰器就可以将未登录用户拒之门外

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
	if request.method == 'POST':
		name = request.form['name']

		if not name or len(name) > 20:
			flash('Invalid input.')
			return redirect(url_for('settings'))

		current_user.name = name
		# current_user 会返回当前登录用户的数据库记录对象
		# 等同于下面的用法
		# user = User.query.first()
		# user.name = name
		db.session.commit()
		flash('Settings updated.')
		return redirect(url_for('index'))
	return render_template('settings.html')

