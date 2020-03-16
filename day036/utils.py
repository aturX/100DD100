def valid_login(username, password):
	users = {
		"lsy": "lsy",
		"fang": "fang",
		"admin": "123456"
	}
	password_db = users.get(username, "")
	if password == password_db:
		return True

	return False


def log_the_user_in(username):
	return "欢迎VIP用户 {} 登录本网站！".format(username)

