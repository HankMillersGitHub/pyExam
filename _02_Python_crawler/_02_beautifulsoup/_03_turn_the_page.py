import time
import requests
from bs4 import BeautifulSoup
from pip._internal.network.utils import HEADERS

base_url = "https://quotes.toscrape.com"
url = base_url
all_quote = []
while url:
    print(f"抓取：{url}")
    resp = requests.get(url,headers=HEADERS,timeout=5)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text,'lxml')
    for q in soup.select("div.quote"):
        all_quote.append({
            "text":q.select_one("span.text").get_text(strip=True),
            "author":q.select_one("small.author").get_text(strip=True)
        })
    next_btn = soup.select_one("li.next a")
    if next_btn:
        url = base_url + next_btn.get("href")
    else:
        url = None
    time.sleep(1) # 限速，减轻被爬网站服务器压力
print(f"共抓取了{len(all_quote)}条数据")
# 持久化爬取数据
# import json
# with open("_03_data_has_been_acquired.json","w",encoding="utf8") as f:
#     json.dump(all_quote,f,ensure_ascii=False,indent=2)
# 保存为csv
# import csv
# with open("_03_data_has_been_acquired.csv","w",newline="",encoding="utf8") as f:
#     writer = csv.DictWriter(f,fieldnames=["text","author"])
#     writer.writeheader()
#     writer.writerows(all_quote)