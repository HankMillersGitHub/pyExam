import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com/"
headers = {
            "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=headers,timeout=5)
# 获取连接状态
resp.raise_for_status()
# 设置连接编码格式
resp.encoding = "utf8"
# 创建beautifulsoup实例
soup = BeautifulSoup(resp.text, "lxml")
divs = soup.select("div.quote")
for div in divs:
    # 获取每个class为quote的div中的class为text的span元素
    text = div.select_one("span.text").get_text(strip=True)
    # 获取每个class为quote的div中的class为author的small元素
    small = div.select_one("small.author").get_text(strip=True)
    # 获取每个class为quote的div中class为tags的div中的class为tag的a元素
    tags = [t.get_text(strip=True) for t in div.select("div.tags a.tag")]
    print(f"quote:{text}")
    print(f"author:{small}")
    print(f"tags:{tags}")
    print("-" * 40)
