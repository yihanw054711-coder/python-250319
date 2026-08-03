"""
    该案例演示了类的定义以及访问类中的成员
"""
class Person:
    """这是一个人的类"""
    home = "earth"
    # def __init__(self):
    #     self.age = 0

    def eat(self):
        print("eating")

    def drink(self):
        print("drinking")

# 引用
print(Person.home)
print(Person.eat)
print(Person.__doc__)

# 实例化
zsf = Person()
print(zsf.home)
# zsf.eat() ==> Person.eat(zsf)
zsf.drink()
Person.eat