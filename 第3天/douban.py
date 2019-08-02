"""
豆瓣电影 Top250 页面链接如下
https://movie.douban.com/top250
我们的 client_ssl.py 已经可以获取 https 的内容了
这页一共有 25 个条目

所以现在的程序就只剩下了解析 HTML

请观察页面的规律，解析出
1，电影名
2，分数
3，评价人数
4，引用语（比如第一部肖申克的救赎中的「希望让人自由。」）

解析方式可以用任意手段，如果你没有想法，用字符串查找匹配比较好(find 特征字符串加切片)
"""
# 获得内容部分 ol
def ollis():
    from my.crawler import get
    # 单页面
    URL = "https://movie.douban.com/top250"

    query = {
        'Accept': 'text/html',
        'Accept - Language': 'zh - CN, zh;q = 0.9, en;q = 0.8',
    }
    status_code, headers, body = get(URL, query)

    # print(body.find("<body>"))
    # print(body.find("</body>"))
    start = body.find("<body>")
    end = body.find("</body>")

    htmlBody = body[start:end]

    start1 = htmlBody.find('<div id="content">')
    end1 = htmlBody.find('<div id="footer">')
    contentTop250 = htmlBody[start1:end1]

    start3 = contentTop250.find('<ol class="grid_view">')
    end3 = contentTop250.find('</ol>')

    olBody = contentTop250[start3:end3]

    with open('./body.html', 'w', encoding='utf-8') as f:
        f.write(olBody)

    return olBody


# 得到每页的内容
def get_items(olBody:str):
    items = []
    count = 0
    while count < 20:
        count += 1
        temp_end = olBody.find("</li>")
        item = olBody[:temp_end]
        olBody = olBody[temp_end+6:]  # 切除 留下后边部分 [去掉上一段li]
        items.append(item)
    return items

# 获取每条信息
def get_info(item:str):
    name = item[item.find('<span class="title">')+len('<span class="title">'): item.find('</span>')]
    people = item[item.find('<p class="">')+len('<p class="">'): item.find('</p>')].strip()
    cent = item[item.find('<span class="rating_num" property="v:average">')+len('<span class="rating_num" property="v:average">'): item.find('<span property="v:best" content="10.0">')].replace("</span>", "")
    item = item[item.find('<span class="inq">')+len('<span class="inq">'):]
    say = item[:item.find('</span>')]

    info = dict(
        name=name,
        people=people,
        cent=cent,
        say=say,
    )
    return info
# 一个豆瓣top250 的爬虫程序  (使用Redis 存储)
olBody = ollis()    # 获得所有内容部分
items = get_items(olBody)    # 获得单条内容
info_20 = []
for item in items:
    item_info = get_info(item)
    info_20.append(item_info)
print(info_20)

# 全页面