"""
    该案例演示了match ... case
    给定月份，输出对应的月有多少天
    ｜是专门用于模式匹配的操作符，他能把多个常量或者模式组合起来，实现“或”的逻辑。
"""
from random import randint
match month := randint(1, 12):
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f"{month}月有31天")
    case 4 | 6 | 9 | 11:
        print(f"{month}月有30天")
    case 2:
        print(f"{month}月可能有28天")
    case _:
        print(f"{month}月有?天")
