from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

def getAlldate():
	url = 'https://adnodoor.com/nav/'
	html = urlopen(url)
	bsObj = BeautifulSoup(html.read(), features="html.parser")
	# print(bsObj)
	# xe-widget xe-conversations box2 label-info
	getBody = bsObj.body
	#print(getBody)

	getDiv = bsObj.findAll("div", {"class": "xe-comment"})
	#print(getDiv)
	alldate = []
	for one in getDiv:
		getName = one.strong.text
		# print(getName)
		# print(getDiv[0])
		getInfo = one.findAll("p", {"class": "overflowClip_2"})[0].text
		# print(getInfo)
		getUrl = one.attrs['onclick'].split("'")[1]
		#print(getUrl)
		date = {}
		date["webName"] = getName
		date["webInfo"] = getInfo
		date["webUrl"] = getUrl
		date["fromUrl"] = url
		alldate.append(date)
		#print(alldate)
	return alldate

def save_csv():
	csvFile = open("./getalldate.csv", 'w+', encoding="utf-8", newline='')
	try:
		writer = csv.writer(csvFile)
		writer.writerow(('序号', '网站名称', '网站描述', '网址', '来源'))
		i = 1
		for one in getAlldate():
			writer.writerow((i, one["webName"], one["webInfo"], one["webUrl"], one["fromUrl"]))
			i = i + 1
	finally:
		csvFile.close()

def save_mysql(data):
	import pymysql

	"""
	insert into searcher_websites (id, webUrl,webName,webDoc,webLogo,webType,cent, fromUrl)
  value(REPLACE(UUID(),'-',''),'https://www.dogedoge.com/','多吉搜索','替代百度的中文搜索引擎','','搜索引擎','100','https://www.dogedoge.com/')
	"""

	conn = pymysql.connect(host='127.0.0.1',
	                       user='root', passwd='root', db='mysql')
	# 使用cursor()方法获取操作游标
	cur = conn.cursor()
	insertSQL = "insert into searcher_websites (id, webUrl,webName,webDoc,webLogo,webType,cent, fromUrl) value(REPLACE(UUID(),'-',''),'{0}','{1}','{2}','','',0,'{3}')"
	try:
		# 写入数据
		for one in data:
			tempSql = insertSQL.format(one["webUrl"], one["webName"], one["webInfo"], one["fromUrl"])
			try:
				cur.execute(tempSql)
				print("写入成功：" + str(one))
			except Exception as e:
				print("写入失败：" + str(one))
		# 提交
		conn.commit()
	except Exception as e:
		# 错误回滚
		print(e)
		conn.rollback()
	cur.execute("SELECT count(*) FROM searcher_websites")
	print(cur.fetchone())
	cur.close()
	conn.close()

if __name__ == "__main__":
	data = getAlldate()
	print(data)
	# save_mysql(data)