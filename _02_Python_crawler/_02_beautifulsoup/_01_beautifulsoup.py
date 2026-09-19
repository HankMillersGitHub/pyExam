from bs4 import BeautifulSoup
# region
# 创建html对象 可以从requests的结果取
html = """
<div class='quote'>
<span class='text'> hello </span>
<small class='author'>Hank</small>
</div>
<div class='demo'></div>
"""
# 创建soup对象用来读取具体数据
soup = BeautifulSoup(html, "lxml")
# 单独寻找元素
# 寻找第一个div标签
# print(soup.find("div"))
# 寻找class名字是quote的第一个div
# print(soup.find("div", class_='quote'))
# 寻找class名字是text的第一个span
# print(soup.find("span", class_='text'))

# region
# 寻找全部元素 并返回元素列表
# divs = soup.find_all("div")
# for div in divs:
#     print(div)
# endregion

# region
# 使用css选择器寻找元素
# soup.select("div.quote") # 返回class名字为quote的div标签
# soup.select("span.text") # 返回class名字为text的span元素
# soup.select("#main") # 返回id为main的所有元素
# soup.select("div.quote span") # 返回class名字为div中的span元素
# soup.select_one("span.text") # 只取第一个class为text的span元素
# endregion

# region
# 获取元素内文本和属性
# span = soup.find("span",class_="text")
# print(span.text) # 获取元素内容
# print(span.get_text(strip=True)) # 获取元素内容并去掉首尾空格
# a = (soup.find("a"))
# print(a["href"]) # 返回a标签中的href属性
# print(a.get("href")) # 返回a标签中的href属性 不存在返回None
# endregion
