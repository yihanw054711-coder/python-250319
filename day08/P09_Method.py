"""
    该案例演示了方法
"""
import types


def drink(self):
    print("drinking")

class Student:
    """这是一个学生类"""
    school = "atguigu"
    def __init__(self, name, age):
        # 定义实例属性    每个实例属性是独立的，互相不影响
        self.name = name
        self.age = age

    # 实例方法  方法第一个参数是self,表示当前实例对象
    # 对象.方法()   调用当前方法的时候，会将当前对象作为参数传递给方法
    def play_game(self):
        print(f"{self.age}岁的{self.name} 正在专注地玩着游戏")

    def study(self):
        print(f"{self.age}岁的{self.name} 正在有一搭没一搭的学习")

    def video(self):
        print(f"{self.age}岁的{self.name} 正在录视频")

    # 类方法
    @classmethod
    def get_info(cls):
        print(cls.school)
        print(cls.__doc__)

zwj = Student("zwj", 23)
# Student.drink = drink
# zwj.drink()
zwj.drink = types.MethodType(drink, zwj)
zwj.drink()  # 张三在吃饭

# Student.get_info()

"""
class Mathutil:
    @staticmethod
    def add(a, b):
        return a + b


print(Mathutil.add(1, 2))
"""