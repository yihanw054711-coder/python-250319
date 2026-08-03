"""
    该案例演示了global和nonlocal关键词
"""
# 通过+=操作赋值，会报错，认为局部变量还未定义
"""
var1 = 100
def function_a():
    #  声明：当前在局部作用域中使用全局的变量var1
    global var1
    var1 = 200
    print(f"局部作用域中的var1={var1, id(var1)}")
function_a()
print(f"全局作用域中的var1={var1,id(var1)}")
"""
"""
def function_a():
    # list1[0] = -1000
    list1 = [3, 4, 5]
    print("list1:", list1)

list1 = [1, 2, 3]
print(list1)  # [1, 2, 3]
function_a()  # list1: [-1000, 2, 3]
print(list1)  # [-1000, 2, 3]
"""
def outer():
    var1 = 10
    def inner():
        nonlocal var1
        var1 = 20
        print(f"局部作用域中的var1={var1, id(var1)}")
    inner()
    print(f"嵌套作用域中的var1={var1, id(var1)}")
outer()

