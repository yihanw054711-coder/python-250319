"""
一、选择题
以下哪种异常通常在尝试访问字典中不存在的键时引发？（A）
A. KeyError

B. IndexError

C. ValueError

D. TypeError

KeyError	当在现有键集合中找不到指定的映射（字典）键时将被引发。
IndexError	当序列抽取超出范围时将被引发。
ValueError  当函数接收到类型正确但值不合适的参数时。
TypeError	当一个操作或函数被应用于类型不适当的对象时将被引发。
"""

"""
以下关于try - except - finally语句的描述，正确的是（B）
A. finally块中的代码只有在没有异常发生时才会执行

B. finally块中的代码无论是否发生异常都会执行

C. 如果try块中发生异常，except块和finally块都不会执行

D. except块和finally块只能存在一个
"""
"""
二、简答题
简述异常处理的作用。
答案：异常处理的作用主要有以下几点：
增强程序的健壮性：当程序运行过程中遇到错误（如除零操作、文件不存在等）时，异常处理机制可以捕获这些错误，避免程序因未处理的错误而崩溃，确保程序能够继续运行或者以一种可控的方式结束。
提高代码的可读性：通过将可能出现错误的代码放在try块中，对应的错误处理代码放在except块中，使得代码结构更加清晰，阅读代码的人能够清楚地知道哪些部分可能出错以及出错后如何处理。
便于调试和维护：异常处理能够提供详细的错误信息，帮助开发者快速定位和解决问题，同时在维护代码时，清晰的异常处理结构有助于理解代码在不同情况下的行为。

自定义异常类通常继承自哪个基类？为什么要继承自这个基类？
答案：自定义异常类通常继承自Exception类。继承自Exception类的原因是，Exception类处于 Python 异常类层次结构的较高层级，它作为所有内置异常类的基类，具有通用性。继承自Exception类可以让自定义异常类自动拥有一些标准的异常特性和行为，同时也方便在try - except语句中与其他内置异常一起进行捕获和处理，使得代码的异常处理逻辑更加统一和规范。
"""
"""
三、编程题
编写一段 Python 代码，尝试将字符串 “123abc” 转换为整数，
如果转换失败，捕获 ValueError 异常，将异常信息记录到一个文本文件 error.log 中。
"""
try:
    int1 = int("123bc")
except ValueError as e:
    with open("error.log.txt", "w") as f:
        f.write(f"{e}")
"""        
定义一个函数check_age，该函数接受一个年龄参数。
如果年龄小于 0，抛出一个自定义异常InvalidAgeError；如果年龄大于 120，抛出UnrealisticAgeError。
这两个自定义异常类都继承自Exception类。调用该函数并传入一个不合法的年龄值，捕获并处理异常。
"""
class InvalidAgeError(Exception):
    pass

class UnrealisticAgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise InvalidAgeError("年龄不能为负数")
    elif age > 120:
        raise UnrealisticAgeError("年龄超过120不太现实")

try:
    check_age(-5)
except (InvalidAgeError, UnrealisticAgeError) as e:
    print(f"[{type(e).__name__}] {e}")




