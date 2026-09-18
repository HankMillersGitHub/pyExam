# try
# try:
#     n = int("abc")
# except ValueError as e:
#     print("转换失败:",e)
from asyncio import print_call_graph

# 多个异常
# try:
#     a = 10 / 0
# except ZeroDivisionError:
#     print("0不能做除数")
# except ValueError:
#     print("值错误")
# except Exception as e:
#     print(f"其他异常：{e}")

# finally/else
# try:
#     f = open("data.txt")
#     content = f.read()
# except FileNotFoundError:
#     print("File not found.")
# else:
#     print(content)
# finally:
#     print("终将成功！！！")

# 抛出异常
# def set_age(age):
#     if age < 0 :
#         raise ValueError("age cannot be negative")
#     return age
# try:
#     set_age(-9)
# except ValueError as e:
#     print(e)