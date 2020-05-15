import requests
from bs4 import BeautifulSoup
import json
import csv


def get_data():
	url = "https://xn--80aesfpebagmfblc0a.xn--p1ai/information/"

	headers = {
	    'Content-Type': "application/json",
	    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
		'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
	}

	response = requests.request("GET", url, headers=headers)
	soup = BeautifulSoup(response.text, "html.parser")
	content = soup.find('cv-spread-overview')
	data = json.loads(content[':spread-data'])
	print(data)
	return data

def save_data(data):
	with open('俄罗斯疫情数据.csv', 'wt', newline="") as f:
		cw = csv.writer(f)
		# 采用writerow()方法
		cw.writerow(["名称", "是否城市", "累计确诊", "治愈", "死亡", "现存确诊"])
		for item in data:
			temp_data = [
				item.get("title"),
				item.get("is_city"),
				item.get("sick"),
				item.get("healed"),
				item.get("died"),
				int(item.get("sick")) - int(item.get("healed")) - int(item.get("died"))
			]
			print(temp_data)
			cw.writerow(temp_data)  # 将列表的每个元素写到csv文件的一行
data = get_data()

save_data(data)

