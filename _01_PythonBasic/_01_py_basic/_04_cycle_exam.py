# 打印1-100的所有偶数
import random

for i in range(1,101):
    if i % 2 == 0:
        print(i)

# 求1-100 的累加
sumNumber = 0
for i in range(1,101):
    sumNumber += i
print(sumNumber)

# 猜数字
randomNumber = random.randint(1,100)
while True:
    iNumber = int(input("please input your number:"))
    if iNumber == randomNumber:
        print("congratulation! you guessed right!")
        break
    elif iNumber > randomNumber:
        print("you guessed bigger")
    else :
        print("you guessed smaller")