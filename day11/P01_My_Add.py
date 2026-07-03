__all__ = ["num","add"] #  内容必须要用引号引起来

num = 100
num1 = 200
_str1="abc"
def add(a, b):
    """求两个数的和"""
    return a + b

if __name__ == "__main__":
    print(__name__)
    print("p01中的代码执行返回的结果：", add(10, 20))