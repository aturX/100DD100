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

if __name__ == "__main__":
	csvFile = open("./getalldate.csv", 'w+',  encoding="utf-8", newline='')
	try:
		writer = csv.writer(csvFile)
		writer.writerow(('序号', '网站名称', '网站描述', '网址', '来源'))
		i = 1
		for one in getAlldate():
			writer.writerow((i, one["webName"], one["webInfo"], one["webUrl"], one["fromUrl"]))
			i = i + 1
	finally:
		csvFile.close()