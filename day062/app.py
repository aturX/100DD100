from aiohttp import web

from model import User
from web import get
import logging;logging.basicConfig(level=logging.INFO)  # 日志配置


@get('/')
def index(request):
	users = yield from User.findAll()
	return {
		'__template__': 'test.html',
		'users': users
	}


# 初始化
def init():
	app = web.Application()
	app.add_routes([web.get('/', index)])
	logging.info('server started at http://127.0.0.1:9527...')
	web.run_app(app, host='127.0.0.1', port=9527)


if __name__ == "__main__":
	init()
