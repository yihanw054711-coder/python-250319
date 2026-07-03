"""
    该案例演示了复用父类中的属性或者方法
"""
class Person:
    """人的类"""

    home = "earth"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("eating...")

class YellowRace(Person):
    """黄种人"""

    color = "yellow"

    def run(self):
        print("runing...")

class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        # 调用父类的方法   方式1:通过super().父类方法名
        super().__init__(name, age)
        self.grade = grade

    def study(self):
        print("先吃再学")
        super().eat()   # 调用父类的方法   方式2:通过super().父类方法名
        # Person.eat(self)  # 子类中调用父类的方法1.通过父类名.父类方法名(self)
        print("studying...")

class ChineseStudent(Student, YellowRace):  # 继承了Student和YellowRace
    """中国学生"""
    def __init__(self, name, age, grade):
        # 调用父类的方法   方式1:通过super().父类方法名
        super().__init__(name, age, grade)

    country = "中国"

y1 = ChineseStudent("张三", 9, "三年级")
print(y1.home, y1.color, y1.country, y1.name, y1.age)
y1.study()
print(ChineseStudent.__mro__)

super()
