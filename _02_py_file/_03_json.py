# import json
# data = {
#     "name":"hank",
#     "age":22,
#     "hobbies":["read books","running"]
# }
# 字典转换成json
# s = json.dumps(data,ensure_ascii=False,indent=2)
# print(s)
# json -> 字典
# d = json.loads(s)
# print(d["name"])

# 读文件
# 将list转换为dict
# def to_dict(name,value):
#     return {name:value}
#
# dataList = [1,2,3,4]
# with open("./docs/_02_json.json", "r",encoding="utf8") as f:
#     content = f.read()
# try:
# ! 这里的loads如果content没有内容会报错误
#     d = json.loads(content)
# except Exception as e:
#     print(f"这里出错了{e}")
# d["dataList"] = dataList
# with open("./docs/_02_json.json", "w",encoding="utf8") as f:
#     json.dump(d,f, ensure_ascii=False, indent=2)

# csv格式
import csv
# rows = [["hank",29],["miller",30]]
# 读文件
# with open("./docs/_02_csv.csv","r",encoding="utf-8") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# 写文件
# with open("./docs/_02_csv.csv","a",newline="",encoding="utf-8") as f:
#     writer = csv.writer(f)
#     for row in rows:
#         writer.writerow(row)

# 字典写入csv
with open("./docs/_02_csv.csv","a",newline="",encoding="utf-8") as f:
    writer = csv.DictWriter(f,fieldnames=["name","age"])
    #writer.writeheader()        # 专门用于写入表头的代码 运行一次就写入一次表头
    writer.writerow({"name":"张三","age":79})