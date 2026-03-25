"""
    该案例演示了运算符
"""
# ～～～～～～算术运算符～～～～～～
# num1 = 10
# num2 = 4
# # + 加
# print(num1 + num2)
# # - 减、或取负
# print(num1 - num2)
# # * 乘
# print(num1 * num2)
# # / 除
# print(num1 - num2)
# # // 取整除
# print(num1 // num2)
# # % 取余
# print(num1 % num2)
# # ** 幂运算
# print(num1 ** 2)

# ~~~~~~~~~~~~~赋值运算符~~~~~~~~~~~~~
# = 赋值
# num1 = 10
# # += 加法赋值
# num1 += 5
# # -= 减法赋值
# num1 -= 5
# # *= 乘法赋值
# num1 *= 5
# # /= 除法赋值
# num1 /= 5
# # //= 取整除赋值
# num1 //= 5
# # %= 模赋值
# num1 %= 5
# # **= 幂赋值
# num1 **= 5
# # ：= 海象运算符，在表达式(赋值表达式无返回值，存在具有返回值的表达式)中同时进行赋值和返回赋值的值。Python3.8版本新增
# print((num2 := num1 * 2) > num1)
# print((2>1)>num1)
# ~~~~~~~~~~~~~比较运算符~~~~~~~~~~~~~
# num1 = 10
# num2 = 20
# # == 相等，比较两者的值
# print(num1 == num2)
# # != 不相等，比较两者的值
# print(num1 != num2)
# # > 大于
# print(num1 > num2)
# # < 小于
# print(num1 < num2)
# # >= 大于等于
# print(num1 >= num2)
# # <= 小于等于
# print(num1 <= num2)

# ~~~~~~~~~~~~~逻辑运算符~~~~~~~~~~~~~
# and 与，连接两个条件，两个条件都满足时结果为True           x and y, 当x为False时返回x的值，否则返回y的值
# or  或，连接两个条件，两个条件至少满足一个时结果为True      x or y, 当x为True时返回x的值，否则返回y的值
# not 非，取反
# b1 = False
# b2 = True

# print(b1 and b2)
# print(b1 or b2)
# print(not b1)

# print(5 and 8)
# print(0 and 8)


# ~~~~~~~~~~~~~位运算符~~~~~~~~~~~~~
# & 按位与，连接两个条件，两个条件都满足时结果为True
# | 按位或，连接两个条件，两个条件至少满足一个时结果为True
# ^ 按位异或，连接两个条件，两个条件满足一个时结果为True
# ~ 按位取反，取反
# num1 = 17
# num2 = 13
# print(f"正数与运算: {num1} & {num2}")
# print(f"{num1:3} : {num1:08b}")# :3表示数字的宽度为3位(默认用空格填充），08b表示数字的二进制宽度为8位（不满8位则用0填充）
# print(f"{num2:3} : {num2:08b}")
# print(f"{num1 & num2:3} : {num1 & num2:08b}")
# print()
# print(f"正数或运算: {num1} | {num2}")
# print(f"{num1:3} : {num1:08b}")
# print(f"{num2:3} : {num2:08b}")
# print(f"{num1 | num2:3} : {num1 | num2:08b}")
# print()
# print(f"正数异或运算: {num1} ^ {num2}")
# print(f"{num1:3} : {num1:08b}")
# print(f"{num2:3} : {num2:08b}")
# print(f"{num1 ^ num2:3} : {num1 ^ num2:08b}")
# print()
# print(f"非运算: ~{num1}")
# print(f"{num1:3}原码: {num1:08b}")
# print(f"{num1:3}取反: {(1 << 8) - 1 ^ num1:08b}，得到结果的补码")# 1 << 8 - 1，得到补码的符号位
# print(f"{~num1:3}原码: {~num1:08b}，计算出结果的原码")
#
# num1 = 17
# num2 = 13
# num3 = -12
#
# print(f"有负数的与运算: {num3} & {num1}")
# print(f"{num3:3}原码 : {num3:08b}")
# print(f"{num3:3}反码 : {(1 << 8) - 1 + num3:08b}")
# print(f"{num3:3}补码 : {(1 << 8) + num3:08b}")
# print(f"{num1:3}补码 : {num1:08b}")
# print(f"{num1 & num3:3}补码 : {num1 & num3:08b}，得到结果")
# print()
#
# print(f"有负数的或运算: {num3} | {num1}")
# print(f"{num3:3}原码 : {num3:08b}")
# print(f"{num3:3}反码 : {(1 << 8) - 1 + num3:08b}")
# print(f"{num3:3}补码 : {(1 << 8) + num3:08b}")
# print(f"{num1:3}补码 : {num1:08b}")
# print(f"{num1 | num3:3}补码 : {(1 << 8) + (num1 | num3):08b}，得到结果的补码")
# print(f"{num1 | num3}原码 : {num1 | num3:08b}，计算出结果的原码")

#
# num1 = 17
# num2 = -12
#
# offset = 1
# print(f"左移运算: {num1} << {offset}")
# print(f"{num1:3} : {num1:08b}")
# print(f"{num1 << offset:3} : {num1 << offset:08b}")
# print()
#
# offset = 2
# print(f"左移运算: {num2} << {offset}")
# print(f"{num2:3}原码\t\t: {num2:08b}")
# print(f"{num2:3}反码\t\t: {(1 << 8) - 1 + num2:08b}")
# print(f"{num2:3}补码\t\t: {(1 << 8) + num2:08b}")
# print(f"{num2:3}补码<<{offset}\t: {(((1 << 8) + num2) << 2) & 0xff:08b}，得到结果的补码")
# print(f"{num2 << offset:3}\t\t\t: {num2 << offset:08b}，计算出原码")
# print()
# print(bin(0xff))
# offset = 3
# print(f"右移运算: {num1} >> {offset}")
# print(f"{num1:3} : {num1:08b}")
# print(f"{num1 >> offset:3} : {num1 >> offset:08b}")
# print()
#
# offset = 3
# print(f"右移运算: {num2} >> {offset}")
# print(f"{num2:3}原码\t\t: {num2:08b}")
# print(f"{num2:3}反码\t\t: {(1 << 8) - 1 + num2:08b}")
# print(f"{num2:3}补码\t\t: {(1 << 8) + num2:08b}")
# print(f"{num2:3}补码>>{offset}\t: {(((1 << 8) + num2) >> offset) | (0xff >> 5 << 5):08b}，得到结果的补码")
# print(f"{num2 >> offset:3}\t\t\t: {num2 >> offset:08b}，计算出原码")

# ~~~~~~~~~~~~~成员运算符~~~~~~~~~~~~~
# in 判断某个元素是否在某个序列中
# num1 =10
# num2 =60
# numbers = [10, 20, 30, 40, 50]
# print(num1 in numbers)
# print(num2 in numbers)

#~~~~~~~~~~~~~~身份运算符~~~~~~~~~~~~~
m = 20
n = 20
q = 30
print(m is n)  # True 判断m和n在内存中是否指向同一个地址
print(n is q)  # False
print(n is not q)  # True
# id() 用于获取对象在内存中的地址
print(id(m) == id(n)) # True

print("-" * 30)
# -------------is和==的区别---------------
a = [1,2,3]
b = a

print(b is a)  # True
print(b == a)  # True

b = a[:]
print(b)
print(b is a)  # False
print(b == a)  # True