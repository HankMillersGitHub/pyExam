# 变量
name = "马中豪"
age = 19

# 数字
a = 10  #整数
b = 20.123   # float
c = 2 + 2j   # complex 复数
print(a + b) # 30.123
print(7 // 2) # 整除符号
print(7 % 2)  # 取余
print(2 ** 3) # 2^3

# 字符串
s1 = 'hello'
s2 = "hello"
s3 = """多行字符串"""
print(s1 + " " + s2)    # 拼接
print(s1.upper())       # 转大写
print(s1.upper().lower())       # 转小写
print(s1.replace('h','H')) # 替换
print(len(s1)) # 字符串长度
print(s1[0],s1[-1]) # 正数正数 负数倒数
print(s1[1:3]) # 切片

# 布尔类型
is_ok = True
is_bad = False
print(10 > 3)       # True
print(10 < 3)       # False
print(not is_ok)    # False

# none
result = None
print(result is None) # True

# 常用类型转换
print(int("123"))
print(float("3.14"))
print(str(100))
print(bool(0))
print(bool(""))
print(bool("abc"))