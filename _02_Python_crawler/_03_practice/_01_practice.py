# 抓每本书的：书名、价格、评分、库存状态
# 翻页，抓所有页
# 保存到 books.csv
import json
import requests,time,csv
from bs4 import BeautifulSoup
from pip._internal.network.utils import HEADERS

base_url = "https://books.toscrape.com/"
url = base_url
# 创建books列表
books = []
while url:
    print(f"抓取：{url}")
    # 请求网站
    resp = requests.get(url,HEADERS,timeout=20)
    # 防止网站连接失效
    resp.raise_for_status()
    # 防止中文乱码
    resp.encoding = "utf8"
    # 使用soup处理获取到的网站数据
    soup = BeautifulSoup(resp.text,'lxml')
    # 遍历拿到的ol 获取需要的数据
    # 书名 ol.row > li > article > h3 > a.text
    # 价格 ol.row > li > article > div.product_price > p.price_color.text
    # 评分 ol.row > li > article > p > i.class[2]
    # 库存 ol.row > li > article > div.product_price > p.availability.class
    # 翻页 ol.pager > li.next > a.href
    for li in soup.select("ol.row li"):
        books.append({
            "title" : li.select_one("h3 a").get("title"),
            "price" : li.select_one("div.product_price p.price_color").text,
            "rating" : li.select_one("p")["class"][1],
            "stock" : li.select_one("div.product_price p.availability")["class"][0]
        })
    # 翻页
    next_btn = soup.select_one("ul.pager li.next a")
    if next_btn:
        address = next_btn.get("href")
        if address.find("catalogue/") is not -1:
            url = base_url + address
        else:
            url = base_url + "catalogue/" + address
    else:
        url = None
    # 持久化到csv中
    with open("./_01_practice.csv","w",newline="",encoding="utf8") as f:
        writer = csv.DictWriter(f,fieldnames=["title","price","rating","stock"])
        writer.writeheader()
        writer.writerows(books)
    time.sleep(0.5)
print(f"共抓取了{len(books)}")
