"""
    该案例演示了self
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("eating")

    def drink(self):
        print("drinking")

    def play(self):
        print("playing")

    def eat_play(self):
        # 在实例方法中调用其他的实例方法
        self.eat() # Student.eat(self)
        self.play() # Student.play(self)

zsf = Student("zsf", 81)
zsf.eat_play()