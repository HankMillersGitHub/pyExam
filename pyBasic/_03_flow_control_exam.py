# 输入年份判断是否闰年
year = int(input("请输入一个年份："))
# 闰年 能被4整除且不能被100整除，或者能被四百整除
if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
    print("闰年")
else:
    print("平年")

# 输入成绩判断是什么等级
score = int(input("please input you score:"))

if score >= 90 :
    print("A")
elif score >= 80 :
    print("B")
elif score >= 70 :
    print("C")
elif score >= 60 :
    print("D")
else:
    print("E")