import time
# 获取时间戳
print(time.time())
time.sleep(3)
# 格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S"))

t = time.localtime()
print(t.tm_year,t.tm_mon,t.tm_mday)