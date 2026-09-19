import ast
import csv

import requests,json
from bs4 import BeautifulSoup
from pip._internal.network.utils import HEADERS
from collections import Counter
# base_url = "https://quotes.toscrape.com"
# url = base_url
# all_quote = []
# while url:
#     print(f"抓取{url}")
#     resp = requests.get(url,HEADERS,timeout=20)
#     resp.raise_for_status()
#     resp.encoding="utf8"
#     soup = BeautifulSoup(resp.text,'lxml')
#     divs = soup.select("div.quote")
#     for div in divs:
#         tags_texts = []
#         tags = div.select_one("div.tags").select("a")
#         for tag in tags:
#             tags_texts.append(tag.get_text())
#         all_quote.append({
#             "title":div.select_one("span.text").get_text(),
#             "author": div.select_one("small.author").get_text(),
#             "tags": tags_texts
#         })
#     next_btn = soup.select_one("ul.pager li.next a")
#     if next_btn:
#         url = base_url + next_btn.get("href")
#     else:
#         url = None
# print(f"共抓取{len(all_quote)}条数据")
# with open("./_02_practice.csv","w",newline="",encoding="utf8") as f:
#     writer = csv.DictWriter(f,fieldnames=["title","author","tags"])
#     writer.writeheader()
#     writer.writerows(all_quote)
# 名言、作者、标签
# 统计每个作者出现多少次
# author_counter = Counter(q["author"] for q in all_quote)
# print(author_counter)
# 统计所有标签，按出现次数排序
all_target = []
with open("./_02_practice.csv","r",encoding="utf8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        all_target.extend(ast.literal_eval(row["tags"]))
tag_counter = Counter(q for q in all_target)
print(tag_counter)
# print(tag_counter.most_common(5))
# print(json.dumps(all_target,ensure_ascii=False,indent=2))
