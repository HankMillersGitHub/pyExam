# 定义函数处理两数相除
def division_of_numbers(a,b):
    try:
        m = int(a)
        n = int(b)
    except ValueError:
        print("cannot process string type")
        return None

    if n == 0:
       raise ZeroDivisionError("division by zero")
    return m / n


try:
    x = input("Enter a dividend: ")
    y = input("Enter a divisor: ")
    print(division_of_numbers(x, y))
except ZeroDivisionError as e:
    print(e)

# 读入不存在的文件捕获异常并打印友好提示
# try:
#     with open("numbers.txt", "r") as f:
#         f.read()
# except FileNotFoundError as e:
#     print(f"this file which be called {e.filename} is not found")