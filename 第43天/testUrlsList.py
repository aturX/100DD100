import unittest

from UrlsList import init_db, app


class UrlsListTestCase(unittest.TestCase):
	# 测试数据库连接
	def test_database_init(self):
		db = init_db(app)
		self.assertIn(r'Engine(sqlite:///D:\app\Ldata\100DD100\第300天\db/data.db)', str(db.engine))


if __name__ == '__main__':
	unittest.main()