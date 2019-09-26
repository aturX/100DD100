from UrlsList import User, db, Website

name = "Lsy"

websites = [
	{
		'name': '百度搜索',
		'url': 'http://www.baidu.com',
		'info': '搜索引擎'
	 },
	{
		'name': '多吉搜索',
		'url': 'https://www.dogedoge.com/',
		'info': '干净的搜索引擎'
	},
	{
		'name': '留言板项目',
		'url': 'http://sayhello.helloflask.com/',
		'info': '用Python + Flask 实现的留言板项目'
	},
	{
		'name': '电影列表项目',
		'url': 'http://watchlist.helloflask.com/',
		'info': '用Python + Flask 实现的电影信息展示列表项目'
	},
	{
		'name': 'Flask入门教程',
		'url': 'https://read.helloflask.com/',
		'info': 'Flask快速上手入门教程'
	},
	{
		'name': '狼牌导航站',
		'url': 'https://www.volf.club/',
		'info': '优秀的导航网站'
	},

]

# 全局的两个变量移动到这个函数内


def add_mock_data(name, websites):

	user = User(name=name)
	db.session.add(user)

	for website in websites:
		toadd_website = Website(name=website['name'], url=website['url'], info=website['info'])
		db.session.add(toadd_website)

	db.session.commit()

add_mock_data(name, websites)