"""
    该案例演示了属性
"""

class Dog:
    home = "earth"

    def __init__(self, name, age):
        self.name = name
        self.age = age

xh = Dog("xh", 22)
print(xh.name)
print(xh.age)
xh.color = "black"
print(xh.color)
print("~"*30)
bg = Dog("bg", 3)
print(bg.home)
print(bg.name)
print(bg.age)

"""
print(Dog.home)
wc = Dog()
print(wc.home)

# 通过 类名.属性名 添加与修改类属性
wc.kemu = "quanke"
Dog.kemu = "quanke"
print(wc.kemu)

dh = Dog()
print(dh.kemu)
"""