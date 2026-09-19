# 类的基础定义
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         return f"my name is {self.name} and my age is {self.age}"
# s = Student("Hank Miller",29)
# print(s.introduce())

# 类属性 和 实例属性
# class Dog:
    # 这里的species就是类属性 所有根据此类实例化的对象都有这个属性
    # species = "dog"
    # def __init__(self,name):
        # 这里的name就是实例属性 每个实例的name属性都不一定相同
        # self.name = name
# d1 = Dog("big yellow")
# d2 = Dog("big black")

# 继承
class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "..."
class Cat(Animal):
    def speak(self):
        return "喵~"
class Tiger(Animal):
    def speak(self):
        return "嗷呜~"

for an in [Cat("旺财"),Tiger("来福")]:
    print(an.speak())