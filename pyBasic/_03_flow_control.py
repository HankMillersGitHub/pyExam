# if elif else
score = 78
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# 逻辑运算
age = 20
has_ticket = True
if age >= 18 and has_ticket:
    print("可以入场")
if age < 18 or not has_ticket:
    print("不可以入场")
result = "成年" if age >= 18 else "未成年"
print(result)