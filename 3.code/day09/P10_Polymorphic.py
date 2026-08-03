"""
    该案例演示了多态
"""
class Bird:
    def __init__(self, name):
        self.name = name

class Fish:
    def __init__(self, name):
        self.name = name

class Dog:
    def __init__(self, name):
        self.name = name

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call(self, flag):
        ani = None
        match flag:
            case "1":
                ani = Bird("红火")
            case "2":
                ani = Fish("小鱼儿")
            case "3":
                ani = Dog("旺财")
        return ani
    def feed(self, ani):
        print(f"{self.name}正在喂养他的小动物{ani.name}")

wf = Person("wf", 18)
# ani = wf.call("3")
# print(ani.name)
B1 = Bird("B1")
wf.feed(B1)
D1 = Dog("D1")
wf.feed(D1)




class Person:

    @property
    def name(self):
        return self.name

p = Person()
p.name  # 报错：RecursionError: maximum recursion depth exceeded

