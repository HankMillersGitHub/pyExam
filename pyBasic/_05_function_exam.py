# 判断素数
def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    for i in range(3,int(num**0.5)+1,2):
        if num % i == 0:
            return False
    return True
num = int(input("enter a number:"))
print(is_prime(num))

# 求阶乘
# def factorial(num):
#     result = 1
#     for i in range(2,num+1):
#         result *= i
#     return result
# print(factorial(5))

# 返回单词出现次数的字典
# def count_words(text):
#     wordsList = text.split(" ")
#     dict = {}
#     for word in wordsList:
#         dict[word] = dict.get(word,0) + 1
#     return dict
# print(count_words("hello world i love you i heat you i bit you"))