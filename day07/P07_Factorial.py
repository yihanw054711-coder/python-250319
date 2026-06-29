"""
    该案例演示了函数的递归
    案例：求一个整数n的阶乘
"""

#  不用递归
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial(500000000000))

"""
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(999))
"""