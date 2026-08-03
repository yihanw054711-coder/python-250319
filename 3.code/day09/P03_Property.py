"""
    该案例演示了封装相关的注解
"""
"""
# @property 将方法转换为属性
class Person:

    def __init__(self, name):
        self.name = name

    @property
    def eat(self):
        print(f"{self.name} is eating...")


p = Person("张三")
# 默认情况下当调用实例方法的时候，必须用对象.方法名(),哪怕没有参数，括号也不能省略
p.eat()
# 如果在方法上加了@property注解，那么在调用实例方法的时候，直接通过对象.方法名即可，后面的括号不用加
p.eat   # 张三 is eating...
"""
# 通过@property注解实现只读属性
class Person:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == "李四":
            print("不许叫李四")
        else:
            self.__name = name

p = Person("张三")
print(p.name)  # 张三

p.name = "李四"  # 提示 “不许叫李四”
print(p.name)  # 张三

p.name = "王五"
print(p.name)  # 王五




