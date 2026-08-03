"""
    该案例演示了断言机制
"""
def int_add(x, y):
    assert isinstance(x, int) and isinstance(y, int), "参数类型错误"
    return x + y
"""    
    if not isinstance(x, int) and isinstance(y, int):
        raise AssertionError(["参数类型错误"])
"""

print(int_add(1, 2))  # 3
print(int_add("1", "2"))  # AssertionError: 参数类型错误
