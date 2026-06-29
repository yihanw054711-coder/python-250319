"""
    该案例演示了global和nonlocal关键词
"""
# 通过+=操作赋值，会报错，认为局部变量还未定义
var1 = 100
def function_a():
    var1 = 200 # 将var1当做局部变量处理，+=得先定义变量
    print(f"局部作用域中的var1={var1}")
function_a()
print(f"全局作用域中的var1={var1}")
