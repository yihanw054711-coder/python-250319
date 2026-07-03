"""
    该案例演示了自定义异常
"""
class MyException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    # 可能发生异常的代码
    raise MyException("这是我自己定义的异常")
except MyException as e:
    # 对异常处理的代码
    print("触发自定义异常:", e.value)
