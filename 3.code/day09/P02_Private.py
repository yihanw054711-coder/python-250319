"""
    该案例演示了封装
"""
class Person:
    __home = "earth"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eat(self):
        print("eating")

    def eat1(self):
        print("eating")
        print(self.__home)
zs = Person("zs", 23)
zs._Person__eat()
