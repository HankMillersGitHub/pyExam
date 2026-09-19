# 列表 有序、可变、可重复
# hobby = ["抽烟","喝酒","烫头"]
# hobby.append("吃饭")  # 末尾添加
# hobby.insert(1,"喝水") # 指定位置添加
# hobby.remove("吃饭") # 删除指定值
# last = hobby.pop() # 弹出末尾元素
# print(hobby)
# print(hobby[1]) # 第1位的元素
# print(hobby[-1]) # 倒数第一个位置的元素
# print(len(hobby)) # 获取列表的长度
# print("喝酒" in hobby) # 判断某元素是否在列表中
# numbers = [1,2,3,4,1,5,56]
# print(numbers.sort) # 排序
# print(numbers.reverse()) #反转列表


# 字典 dict 键值对的形式存储，键唯一
# students.json = {'name':'张三','age':18,'city':'临汾'}
# print(students.json["name"]) # 不存在返回0
# students.json["score"] = 81 # 新增或修改值
# del students.json['city'] # 删除该键对应的键值对
# print(students.json.keys())  #所有key
# print(students.json.values())  #所有value
# print(students.json.items())  #所有键值对
# for k,v in students.json.items():
#     print(k," => ",v)


# 元组 tuple 有序 不可变
# point = (1,4)
# x,y = point     # 解包
# print(x,y)      #1 4
# # point[0] = 2  报错  元组不可更改
# t = (1,) # 单元素元组要加逗号


# 集合 set 无序、不重复
nums = {1,2,3,4,5,6,6}
print(nums) # 输出1 2 3 4 5 6
a = {1,2,3}
b = {4,5,6}
print(a | b) # 并集
print(a & b) # 交集
print(a - b) # 差集
# 列表去重可以使用set转换然后转回list
numbers = {1,2,3,4,5,6,7,1,1,1,1,1}
print(list(set(numbers))) 
