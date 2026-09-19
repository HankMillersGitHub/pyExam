import requests
# url = "https://quotes.toscrape.com"
# resp = requests.get(url)
# resp常用方法
# print("状态码：")
# print(requests.status_codes)
# print("字符串响应内容：")
# print(resp.text[:500])
# print("字节相应内容 用于下载图片：")
# print(resp.content)
# print("如果返回的是json 直接转为字典")
# print(resp.json())
# print("最终请求的url（可能被重定向过）")
# print(resp.url)
# print("响应头")
# print(resp.headers)
# 如果状态码不是200就抛出异常
# print(resp.raise_for_status())

# region
# 请求头
# 网站会检查User_Agent 不加可能会返回403
# headers = {
#     "User_Agent": "Mozilla/5.0""AppleWebKit/537.36(KHTML,like Gecko) ""Chrome/120.0.0.0 Safari/537.36"
# }
# resp1 = requests.get(url, headers=headers)
# print(resp1.headers)
# endregion

# region
# 超时timeout
# resp = requests.get(url,timeout=5)
# endregion

# region
# 传参
# get传参
# params = {"userName":"zhangsan","password":"123123"}
# resp = requests.get(url, params=params)
# endregion

# region
# 一次完整的请求模板
# url = "http://httpbin.org/get"
# headers = {
#     "User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                   "AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/120.0.0.0 Safari/537.36"
# }
# try:
#     resp = requests.get(url, headers=headers, timeout=5)
#     resp.raise_for_status()
#     resp.encoding = "utf-8" # 防止中文乱码
#     html = resp.text
#     print(len(html))
# except requests.RequestException as e:
#     print(f"请求失败{e}")
# endregion
