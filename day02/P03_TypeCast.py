
"""
    该案例演示了类型转换
"""
#自动类型转换
# num1 = 10
# num2 = 15.5
# print(type(num1),type(num2))
#
# num3 = num1 + num2
# print(type(num3))

# num1 = 5
# num2 = 1
# num3 = num1 / num2
# print(num3)
# print(type(num3))

# num1 = 10
# num2 = "20"
# print(type(num1))
# print(type(num2))
# print(num1 + num2)#会报错

# 通过各种不同的函数实现类型转换（下述函数中带有的"[]"表示其内的是可选参数）
# int(x [,base])    将x转换为一个整数，x若为字符串可用base指定x的进制
# num1 =int("10",2) # 将二进制数10转换为十进制整数
# print(num1)
# print(type(num1))
# float(x) 将x转换为一个浮点数
# num1 = float("5.0")
# print(type(num1))
# complex(real [,imag]) 创建一个实部为real,虚部为img的复数
# num1 = complex(2,3)
# print(num1)
# print(type(num1))

# str1 = "hello world"
# str(x) 将对象转换为一个字符串
# print(str(str1))
# repr(x) 将对象x转换为一个字符串，可以转义字符串中的特殊字符
# print(repr(str1))

# eval(x) 执行x字符串表达式，并返回表达式的值
# print("2+3")
# print(eval("2+3"))

# bin(x) 将一个整数转换为一个二进制字符串
# oct(x) 将一个整数转换为一个八进制字符串
# hex(x) 将一个整数转换为一个十六进制字符串

# ord(x) 将一个字符转换为它的ASCII参数值
print(ord("a"))
# chr(x) 将一个整数转换为一个Unicode字符
print(chr(97))

