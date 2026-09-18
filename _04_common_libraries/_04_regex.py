import re
text = "'celebration' my phone number is 15536836282,email is m18335784129@163.com"
# 查找符合格式的字符串
# m = re.search(r"\w{11}",text)

# 全部匹配
m = re.findall(r"\d{11}",text)
print(m)

# 替换
# print(re.sub(r"\d", "*", text))

# 常用模式
# \d 数字 \w 字母数字下划线 \s 空白
# . 任意字符 * 0+ + 1+ ? 0/1
# ^开头 $ 结尾
