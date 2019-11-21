

"""
网络数据采集 - 爬虫
实现： 爬取  http://webstack.cc/cn/index.html  的数据

结果集保存在 Excel中
结果参数：    网站名称、网址URL、网站描述、图片logo 下载
压缩成zip包


"""
from urllib.error import HTTPError


def step1():
	from urllib.request import urlopen
	# 尝试使用 urllib 原生库
	html = urlopen("http://webstack.cc/cn/index.html")
	print(html.read())

def step2():
	from urllib.request import urlopen
	from bs4 import BeautifulSoup
	html = urlopen("http://webstack.cc/cn/index.html")
	bsObj = BeautifulSoup(html.read(),features="html.parser")
	#title = bsObj.head.title.text
	#print(title)

def step3():
	# 异常处理 保持稳定性
	from urllib.request import urlopen
	from bs4 import BeautifulSoup
	try:
		html = urlopen("http://webstack.cc/cn/index.html")
	except HTTPError as e:
		print(e)
	else:
		bsObj = BeautifulSoup(html.read(), features="html.parser")
	# 检查  标题 是否存在
		try:
			titleContent = bsObj.head.title.text
		except AttributeError as e:
			print("Tag was not found")
		else:
			if titleContent == None:
				print("Tag was not found")
			else:
				print(titleContent)



from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
	"""
	获取 标题
	:param url:
	:return:
	"""
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read(), features="html.parser")
		title = bsObj.head.title.text
	except AttributeError as e:
		return None
	return title

def getHTML(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read(), features="html.parser")
	except AttributeError as e:
		return None
	return bsObj

# 获取数据
def getData(url):
	"""

	:param url:
	:return:
	"""
	title = getTitle(url)
	if title == None:
		print("标题不存在")
	else:
		print(title)

	HTML = getHTML(url)
	# xe-widget xe-conversations box2 label-info
	tableList = HTML.findAll("div", {"class": "xe-widget xe-conversations box2 label-info"})

	data = []
	for table in tableList:
		website = {}
		webName = table.strong.text
		webInfo = table.div.p.text
		# 获得属性  myTag.attrs
		webUrl = table.attrs["data-original-title"]
		website["webName"] = webName
		website["webInfo"] = webInfo
		website["webUrl"] = webUrl
		website["fromUrl"] = url
		data.append(website)
	return data

# 存储数据
def saveData_CSV(data):
	import csv
	csvFile = open("./webstack.csv", 'w+',  encoding="utf-8", newline='')
	try:
		writer = csv.writer(csvFile)
		writer.writerow(('序号', '网站名称', '网站描述', '网址', '来源'))
		i = 1
		for one in data:
			writer.writerow((i, one["webName"], one["webInfo"], one["webUrl"], one["fromUrl"]))
			i = i + 1
	finally:
		csvFile.close()





if __name__ == "__main__":
	url = "http://webstack.cc/cn/index.html"
	# url = "http://www.baidu.com"
	data = getData(url)
	print(len(data))
	saveData_CSV(data)