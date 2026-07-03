"""
题目 1：封装特性
定义一个 BankAccount 类，有一个私有属性 __balance（初始余额为 0），
提供一个 deposit 方法用于存钱，一个 withdraw 方法用于取钱，取钱时如果余额不足则打印提示信息。
"""
import math


class BankAccount():
    def __init__(self):
        self.__balance = 0
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self.__balance}")
    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"{self.__balance}")
        else:
            print("余额不足或者信息不合法")
m1= BankAccount()
m1.withdraw(200)
"""
题目 2：继承特性
定义一个 Animal 类，有一个 speak 方法打印 “I am an animal”。
再定义一个 Cat 类继承自 Animal 类，并重写 speak 方法打印 “Meow”，
创建 Cat 类的对象并调用 speak 方法。
"""
class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("I am an animal")
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print("Meow")
c1 = Cat("c1")
c1.speak()
print(Cat.__mro__)

"""
题目 3：多态特性
定义一个 Shape 类，有一个抽象方法 area（方法体为空）。
再定义 Rectangle 类和 Circle 类继承自 Shape 类，
分别实现 area 方法计算矩形面积（长 × 宽）和圆的面积（(pi r^2)）。
创建 Rectangle 和 Circle 类的对象，将它们放入一个列表中，遍历列表并调用每个对象的 area 方法。
"""
class Shape:
    def __init__(self):
        pass
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, len, wid):
        self.len = len
        self.wid = wid
    def area(self):
        s = self.len * self.wid
        return  s

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        s = math.pi * (self.r ** 2)
        return  s
shapes = [Rectangle(5, 10), Circle(5)]
for shape in shapes:
    print(shape.area())
