# 读文件
# * 方式一 手动关闭
# f = open("./docs/_01_test.txt","r",encoding="utf8")
# content = f.read()
# f.close()
# print(content)

# * 方式二 推荐方式
# with open("./docs/_01_test.txt","r",encoding="utf-8") as f:
#     content = f.read()
# print(content)

# * 按行读取
# with open("./docs/_01_test.txt","r",encoding="utf-8") as f:
#     for line in f:
#         print(f"---{line.strip()}")

# 写文件
# 读写模式
# r           只读，文件必须存在
# w           覆盖写，如果不存在则创建文件
# a           追加写
# r+          读写
# rb/wb       二进制读写
with open("./docs/_01_test.txt","a",encoding="utf8") as f:
    f.write("this is write words\n")