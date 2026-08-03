"""
    该案例演示了方法的重写
"""
class Person:

    home = "earth"

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eating...")

class Chinese(Person):

    color = "yellow"

    # 重写父类方法
    def eat(self):
        print("用筷子吃")

y1 = Chinese("张三")
y1.eat()
