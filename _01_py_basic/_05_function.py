# 基础函数定义
# def greet(name):
#     return f"hello {name}"
# msg = greet("hank")
# print(msg)

# 带参数的函数
# 默认参数
# def greet(name,greeting='hello'):
#     return f"{greeting},{name}"
# print(greet("hank"))
# print(greet("miller","thank you"))
# 关键字参数，在调用参数时 带上定义参数时的参数名可以不用顾及参数顺序
# print(greet(greeting="reverse", name='qjf'))

# 不定长参数
# def add(*args): # 一个星号，参数位置会被打包成元组
#     return sum(args)
# def show(**kwargs): # 参数位置打包成字段，前提是实参是关键字参数
#     for k,v in kwargs.items():
#         print(k,v)
# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(show(a=1, b=2, c=3))

# 函数的返回值
def div(a,b):
    if b == 0:
        return None
    else :
        return a / b
# 返回多个值
def min_max(nums):
    return min(nums),max(nums)
lo,hi = min_max([1,2,3,45,6,7])
print(lo,hi)
