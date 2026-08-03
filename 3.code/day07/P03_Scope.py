"""
    该案例演示了函数的作用域
    局部作用域-->嵌套作用域-->全局作用域-->内建作用域
"""
"""
#  内建作用域，python本身给我们提供的，在所有的模块中的任意位置都可以访问
a = int("10")

# 全局作用域 在当前模块中的任意位置都可以访问
b = 20

def outer():
    #  嵌套作用域 在闭包函数中访问
    c = 30
    def inner():
        # 局部作用域 只能在当前函数的内部访问
        d = 40
        print(a, b, c, d)
    return inner
inn = outer()
inn()



def inner():
    # 局部作用域 只能在当前函数的内部访问
    d = 40
    print(d)
"""
num = 20
# if num <100:
#     msg = "hello"
#     print(msg)

def func():
    if num < 100:
        msg = "hello"
        print(msg)
print(num)
print(msg)


