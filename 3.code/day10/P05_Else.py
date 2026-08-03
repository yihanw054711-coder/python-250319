"""
    该案例演示了else
"""
try:
    result = 10 / 1
except ZeroDivisionError:
    print("除数不能为零！")
else:
    print(f"结果是：{result}")