"""
    该案例演示了参数传递的方式
"""
"""
# 必须参数：按照参数的位置进行匹配  要求：参数的个数必须一致，参数的顺序必须一样
def func(a, b, c):
    print(a, b, c)

func(1, 2, 3)
"""
"""
# 关键字参数（名称传参）   在调用函数传参的时候，指定参数的名字，通过名称和形参进行匹配  形参和实参的顺序可以不一样
def func(name, age):
    print(f"当前用户：{name}, 芳龄:{age}")

# func("zs", 20)
func(age = 18, name = "zs")
"""
"""
# 参数默认值
def func(name, age = 20):
    print(f"当前用户：{name}, 芳龄:{age}")

# func("ls")
func(name = "ls", age = 18)
"""
"""
# 不定长参数
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 如果形参中出现了不定长参数，那么在调用函数的时候，先通过位置进行必须参数的匹配，然后不定长参数后面的参数必须通过关键字参数匹配
def func(num, *args, num1):
    print(num)
    print(args)
    print(num1)

func(3, 2,1,1, num1 = 100)
"""
"""
def func(num, **args):
    print(num)
    print(args)


func(100,a = 1,b = 2,c = 3,d = 4,e = 5)
"""

"""
# 解包传参
def func(a, b, c):
    return a + b + c
tuple11 = (1, 2, 3)
print(func(*tuple11))
# 字典中key的名称和参数名必须一致
dict1 = {"a": 1, "b": 2, "c": 3}
print(func(**dict1))
"""
"""
def func(num, *args):
    print(num)
    print(args)

func(3,*(2,1,1,1))
"""
"""
def func(num, **args):
    print(num)
    print(args)

func(3, **dict(age = "1"))
"""
"""
def func(**args):
    print(args)

func(**dict(age = 1, name = "zs"))
"""
# / 前的参数必须使用位置传参，* 后的参数必须用关键字传参
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

f(1, 2, c=3, d=4, e=5, f=6)






