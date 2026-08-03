
"""
该案例演示了数据类型
"""
#如果数字比较大可以用下划线优化
num1 = 100_000_000
print(num1)

num1 = 10
num2 = True

# type(参数) 查看参数对应的数据类型是什么
# isinstance(参数，数据类型) 判断变量的类型
# print(num1)
# print(num2)
# print(type(num1))
# print(type(num2))
print(isinstance(num2,bool))
# print(isinstance(num1,int))
#~~~~~~~~~~~~~小整数池~~~~~~~~~~~~~~~~~~~~~~~~~
num1 = 3
num2 = 30
# id（） 获取变量值在内存中的地址
print(id(num1))
print(id(num2))
#~~~~~~~~~~~~~浮点数~~~~~~~~~~~~~~~~~
num1 = 0.1
num2 = 0.2
num3 = num1 + num2
# 注意：在任何编程语言中，浮点数类型都存在丢失精度的情况
# print(num1+num2) #0.30000000000000004
# print(type(num3))

#为了解决浮点数丢失精度情况，可以借助python其他模块提供的功能
# from decimal import Decimal
# num1 = Decimal('0.1')
# num2 = Decimal('0.2')
# num3 = num1 + num2
# print(num3)

#~~~~~~~~~~~~~~~布尔~~~~~~~~~~~~~~~~~~~~~~~
num1 = True
num2 = False
print(num1, num2)
print(type(num1),type(num2))

#bool是int的子类型，可以和整数进行运算
print(num1 + 10)

# ==比较运算符  判断==左右两边的值是不是相等
print(num1 == 1)
print(num2 == 0)

#is 判断左右两边是否属于内存中的同一个地址
print(num1 is 1)
print(num2 is 0)
