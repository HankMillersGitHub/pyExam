import os, time, random, re

# 用os列出当前目录全部python程序
# allFile = os.listdir()
# pyFiles = [f for f in allFile if f.endswith(".py")]
# print(pyFiles)

# random抽奖程序
# bingoNumber = random.randint(1, 100)
# while True:
#     userNumber = input("please enter a number between 1 to 100")
#     try:
#         userNumber = int(userNumber)
#     except ValueError:
#         print("please enter a number")
#         continue
#     if userNumber == bingoNumber:
#         print("congratulation,you got it")
#         break
#     elif userNumber > bingoNumber:
#         print("you guess bigger")
#     else:
#         print("you guess smaller")

# 使用正则表达式从文字中提取所有手机号
# text = "this is my phone number : 15536836282,and my email address is m18335784129@163.com"
# phoneNumber = re.findall(r"\b(1[3-9]\d{9})\b",text)
# print(phoneNumber)

# 倒计时
# for i in range(10):
#     print(10 - i)
#     time.sleep(1)
# 直接用range倒数
# for i in range(10,0,-1):
#     print(i)
#     time.sleep(1)