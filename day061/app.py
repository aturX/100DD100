from aiohttp import web
import logging;logging.basicConfig(level=logging.INFO)  # 日志配置


# 路由管理
routes = web.RouteTableDef()

# Controller
@routes.get('/')
def index(request):
	return web.Response(body=b'<h1>Matemask Login Demo</h1>', content_type='text/html')


# 初始化
def init():
	app = web.Application()
	app.add_routes([web.get('/', index)])
	logging.info('server started at http://127.0.0.1:9527...')
	web.run_app(app, host='127.0.0.1', port=9527)

if __name__ == "__main__":
	init()