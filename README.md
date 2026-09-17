# 1. 变量、数字、字符串、布尔、None

## 核心概念

Python 是动态类型语言，变量不需要声明类型，直接赋值。

python

```
# 变量：给值起个名字
name = "小明"
age = 18

# 数字
a = 10          # int 整数
b = 3.14        # float 浮点数
c = 2 + 3j      # complex 复数（了解即可）

print(a + b)    # 13.14
print(7 // 2)   # 3  整除
print(7 % 2)    # 1  取余
print(2 ** 3)   # 8  幂

# 字符串
s1 = 'hello'
s2 = "world"
s3 = """多行
字符串"""
print(s1 + " " + s2)      # 拼接
print(s1.upper())          # HELLO
print(s1.replace("h", "H"))# Hello
print(len(s1))             # 5
print(s1[0], s1[-1])       # h o
print(s1[1:4])             # ell 切片

# 布尔
is_ok = True
is_bad = False
print(10 > 3)      # True
print(10 == 3)     # False
print(not is_ok)   # False

# None：表示“空”，不是 0，也不是空字符串
result = None
print(result is None)   # True
```



## 常用类型转换

python

```
int("123")      # 123
float("3.14")   # 3.14
str(100)        # "100"
bool(0)         # False
bool("")        # False
bool("abc")     # True
```



## 小练习

1. 定义变量存你的姓名、年龄、身高，打印一句话介绍自己。
2. 输入一个三位数，输出它的百位、十位、个位。

------

# 2. 列表 list、字典 dict、元组 tuple、集合 set

## 列表 list：有序、可变、可重复

python

```
fruits = ["apple", "banana", "cherry"]

fruits.append("orange")     # 末尾添加
fruits.insert(1, "pear")    # 指定位置插入
fruits.remove("banana")     # 删除指定值
last = fruits.pop()         # 弹出末尾
print(fruits[0])            # apple
print(fruits[-1])           # 最后一个
print(len(fruits))          # 长度
print("apple" in fruits)    # True
fruits.sort()               # 排序
fruits.reverse()            # 反转
```



## 字典 dict：键值对，键唯一

python

```
student = {"name": "小明", "age": 18, "city": "武汉"}

print(student["name"])              # 小明
print(student.get("score", 0))      # 不存在返回默认值 0
student["score"] = 95               # 新增/修改
del student["city"]                 # 删除
print(student.keys())               # 所有键
print(student.values())             # 所有值
print(student.items())              # 键值对

for k, v in student.items():
    print(k, "=>", v)
```



## 元组 tuple：有序、不可变

python

```
point = (3, 5)
x, y = point        # 解包
print(x, y)         # 3 5

# point[0] = 10    # 报错，元组不能改

# 单元素元组要加逗号
t = (1,)
```



## 集合 set：无序、不重复

python

```
nums = {1, 2, 2, 3, 3, 3}
print(nums)                 # {1, 2, 3}

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)                # 并集 {1,2,3,4,5}
print(a & b)                # 交集 {3}
print(a - b)                # 差集 {1,2}

# 去重常用
names = ["a", "b", "a", "c"]
print(list(set(names)))     # ['a','b','c'] 顺序不保证
```



## 小练习

1. 用列表存 5 个成绩，求平均分、最高分。
2. 用字典存 3 个学生的姓名和分数，打印分数最高的学生。
3. 用集合把两个列表的重复元素找出来。

------

# 3. if / elif / else

## 核心概念

按条件从上往下判断，命中一个就结束。

python

```
score = 85

if score >= 90:
    print("优秀")
elif score >= 75:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```



## 逻辑运算

python

```
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("可以入场")

if age < 18 or not has_ticket:
    print("不能入场")

# 三元表达式
result = "成年" if age >= 18 else "未成年"
print(result)
```



## 嵌套

python

```
x = 10
if x > 0:
    if x % 2 == 0:
        print("正偶数")
    else:
        print("正奇数")
else:
    print("非正数")
```



## 小练习

1. 输入一个年份，判断是否闰年（能被4整除且不能被100整除，或能被400整除）。
2. 输入成绩，输出等级 A/B/C/D/F。

------

# 4. for / while

## for：遍历序列

python

```
# 遍历列表
for fruit in ["apple", "banana"]:
    print(fruit)

# range
for i in range(5):        # 0~4
    print(i)

for i in range(1, 6):     # 1~5
    print(i)

for i in range(0, 10, 2): # 0,2,4,6,8
    print(i)

# 遍历字典
d = {"a": 1, "b": 2}
for k, v in d.items():
    print(k, v)

# 带索引
for i, fruit in enumerate(["a", "b", "c"]):
    print(i, fruit)

# 同时遍历两个列表
for x, y in zip([1, 2, 3], ["a", "b", "c"]):
    print(x, y)
```



## while：条件为真就一直循环

python

```
count = 0
while count < 5:
    print(count)
    count += 1

# 死循环 + break
while True:
    cmd = input("输入 q 退出：")
    if cmd == "q":
        break
```



## break / continue / else

python

```
for i in range(10):
    if i == 3:
        continue    # 跳过本次
    if i == 7:
        break       # 结束循环
    print(i)

# for-else：循环正常结束（没 break）时执行
for i in range(3):
    print(i)
else:
    print("循环结束")
```



## 小练习

1. 打印 1~100 的所有偶数。
2. 求 1+2+...+100。
3. 猜数字：随机生成 1~100，让用户一直猜，直到猜中。

------

# 5. 函数：def、参数、return

## 基础

python

```
def greet(name):
    return f"你好，{name}"

msg = greet("小明")
print(msg)
```



## 参数类型

python

```
# 默认参数
def greet(name, greeting="你好"):
    return f"{greeting}，{name}"

greet("小明")             # 你好，小明
greet("Tom", "Hello")     # Hello，Tom

# 关键字参数
greet(greeting="Hi", name="Tom")

# 不定长参数
def add(*args):           # 位置参数打包成元组
    return sum(args)

def show(**kwargs):       # 关键字参数打包成字典
    for k, v in kwargs.items():
        print(k, v)

add(1, 2, 3)              # 6
show(a=1, b=2)
```



## 返回值

python

```
def div(a, b):
    if b == 0:
        return None
    return a / b

# 返回多个值（其实是元组）
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 5, 2])
```



## 作用域

python

```
x = 10

def f():
    x = 20      # 局部变量，不影响外面
    print(x)

f()             # 20
print(x)        # 10
```



## 小练习

1. 写函数 `is_prime(n)` 判断素数。
2. 写函数 `factorial(n)` 求阶乘。
3. 写函数 `count_words(text)` 返回单词出现次数字典。

------

# 6. 模块：import、pip、venv

## import

python

```
import math
print(math.sqrt(16))     # 4.0

from math import sqrt, pi
print(sqrt(25), pi)

import math as m
print(m.floor(3.7))      # 3

# 自己的模块：新建 mytool.py
# def add(a, b): return a + b
import mytool
print(mytool.add(1, 2))
```



## pip：装第三方库

bash

```
pip install requests
pip install requests==2.31.0
pip install -r requirements.txt
pip uninstall requests
pip list
pip freeze > requirements.txt
```



## venv：虚拟环境

bash

```
# 创建
python -m venv .venv

# 激活
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS/Linux

# 退出
deactivate
```



为什么要用：每个项目独立依赖，互不污染。

## 小练习

1. 新建 `calc.py`，写 `add`、`sub` 函数。
2. 新建 `main.py`，import 进来调用。
3. 创建虚拟环境，安装 `requests`，运行 `import requests`。