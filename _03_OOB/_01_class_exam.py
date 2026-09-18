# 写Book类 有三个属性title author price 一个方法
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def info(self):
        print(f"book name is {self.title} author is {self.author} price is {self.price}")
# BankAccount类 三个方法 存钱 取钱 查余额
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if amount > self.balance:
            print("your balance is not enough!")
        else:
            self.balance -= amount
    def check_balance(self):
        return self.balance