"""
✅已上线	牛导航 - 实用工具导航	http://ziliao6.com/
✅已上线	高效搜罗 - 精准的职业导航	http://gaoxiaosouluo.cn/
✅已上线	卖家大全 - 最全卖家导航	http://maijiadaquan.com/
✅已上线	广告人导航 - 广告没门	https://adnodoor.com/nav/

✅已上线	域名购买&域名商场&行业导航	http://www.yichushou.com/

✅已上线	DreamThere - 梦想导航	https://nav.dreamthere.com/

✅已上线	推荐短视频 - 网红短视频导航	https://wx.dreamthere.com/
✅已上线	狼牌工作网址导航	https://www.volf.club/
✅已上线	JKnear导航 - 建筑结构设计导航	http://jk.jknear.com:777/
✅已上线	site navigation – QAOZEN	https://qaozen.com/nav/
✅已上线	京东运营网址导航	http://miyue1980.com/
✅已上线	快导航 - 简单的网址导航大全	https://wukandy.cn/
✅已上线	ShareHub - 资源和工具的集合	https://www.gezhipu.com/cn/index.html
✅已上线	喵帕斯 - 喵帕斯导航页	http://naspro.cc/
✅已上线	我的收藏夹 - 个人网址导航站	https://www.kukiliao.com/
✅已上线	tool - wxuegao	http://tool.wxuegao.com/
✅已上线	vv.lc - 网址导航	http://vv.lc/
✅已上线	程序员网址导航 - hujiangtao	https://web.hujiangtao.cn/
✅已上线	酸奶 - 广告运营从业者类别导航	酸奶 - 专注广告运营从业者类别导航
✅已上线	浮生论坛 - 念念不忘，必有回响	浮生论坛 - 念念不忘，必有回响
✅已上线	Pandaroll.cn 网址导航	Pandaroll.cn 网址导航
🕗开发中	QAdoc - 测试工作者导航	http://nav.qadoc.org/cn/index.html
🕗开发中	t.hiihi	http://t.hiihi.cn/
🕗开发中	zou0	http://www.zou0.com/cn/index.html
🕗开发中	Matrix Navigation	Matrix Navigation -
🕗开发中	PMGEEK	http://pmgeek.net/
🕗开发中	lerso.cn	http://lerso.cn/
🕗开发中	dh.wdj.pw	WebStack.cc - 设计师网址导航
🕗开发中	wukandy.cn	https://wukandy.cn/


"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getHTML(url):
	html = urlopen(url)
	bs = BeautifulSoup(html.read(), features="html.parser")
	return bs


def getData(url):
	bs = getHTML(url)
	titleContent = bs.head.title.text
	#print(bs)
	body = bs.find_all("body")[0]

	cards = body.findAll("div", {"class": "col-sm-3"})
	print("数量：" + str(len(cards)))

	data = []
	for one in cards:
		website = {}
		webUrlDiv = one.findAll("div", {"class": "xe-widget xe-conversations box2 label-info"})
		webUrl = webUrlDiv[0].attrs["data-link"]

		# print(one)
		webName = one.strong.text
		webInfo = one.findAll("p", {"class": "overflowClip_2"})[0].text.replace(' ','').replace('\n','')
		website["webName"] = webName
		website["webInfo"] = webInfo
		website["webUrl"] = webUrl
		print(website)
		data.append(website)
		print("*"*10)
	return data


if __name__ == "__main__":



	data = getData("http://maijiadaquan.com/")
	print(data)

	import csv
	csvFile = open("./taobao.csv", 'w+',  encoding="utf-8", newline='')
	writer = csv.writer(csvFile)
	writer.writerow(('序号', '网站名称', '网站描述', '网址', '来源'))
	i = 1
	for one in data:
		writer.writerow((i, one["webName"], one["webInfo"], one["webUrl"], "http://maijiadaquan.com/"))
		i = i + 1
	csvFile.close()