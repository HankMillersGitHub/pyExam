import random
# 获取0-1的随机数
print(random.random())
# 获取1-10的整数
print(random.randint(1, 10))
# 在列表中随机选择
print(random.choice([1, 2, 3, 4, 5, 6]))
# 随机排序
nums = [1,2,3,4,5,6,7,8,9]
random.shuffle(nums)
print(nums)
# 随机取两个
print(random.sample(nums, 2))