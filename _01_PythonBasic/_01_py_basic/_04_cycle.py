# for 遍历
# 遍历列表
# fruits = ["apple","orange","pear","beach"]
# for fruit in fruits:
#     print(fruit)
from sqlalchemy.util import format_argspec_init

# 遍历range
# for i in range(5):
#     print(i)
# for i in range(1,6):
#     print(i)
# for i in range(0,10,2):
#     print(i)

# 遍历字典
# d = {"a":1,"b":2,"c":3,"d":4,"e":5}
# for key,value in d.items():
#     print(key,value)

# 遍历并且带索引
# for i,fruit in enumerate(["a","b","c"]):
#     print(i,fruit)

# 同时遍历两个列表
# for x,y in zip([1,2,3],["a","b","c"]):
#     print(x,y)


# while 循环 条件为真就一直循环
count = 0
while count < 5:
    count = count + 1

# 死循环 + break
while True:
    cmd = input("please input 'q' to quit:")
    if cmd == 'q':
        break
