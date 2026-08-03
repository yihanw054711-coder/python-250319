"""
    该案例演示了迭代器
"""
"""
# 演示大部分容器类型都是可以通过for进行遍历的，我们称其为可迭代类型
import os

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {"one": 1, "two": 2}:
    print(key)
for char in "123":
    print(char)

with open("myfile.txt", "w") as f:
    f.write("H\ne\nl\nl\no\n \nW\no\nr\nl\nd\n")
for line in open("myfile.txt"):
    print(line, end="")
os.remove("myfile.txt")
"""
"""
# 判断是否为可迭代类型
from collections.abc import Iterable
print(isinstance([], Iterable))  # True
print(isinstance((), Iterable))  # True
print(isinstance(set(), Iterable))  # True
print(isinstance({}, Iterable))  # True
print(isinstance("100", Iterable))  # True
print(isinstance(100, Iterable))  # False
"""
"""
from collections.abc import Iterator
print(isinstance([], Iterator))  # False
print(isinstance((), Iterator))  # False
print(isinstance(set(), Iterator))  # False
print(isinstance({}, Iterator))  # False
print(isinstance("100", Iterator))  # False
print(isinstance((x for x in range(10)), Iterator))  # True
"""
"""
# 自己通过容器创建迭代器对象
from collections.abc import Iterator
list = [1, 2, 3]
it = iter(list)  # 创建迭代器对象
print(isinstance(it,Iterator))
print(next(it))  # 输出迭代器的下一个元素,1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # StopIteration
"""
# 自定义迭代器    实现容器中元素的反转功能
from collections.abc import Iterator
from collections.abc import Iterable
class Reverse:
    # data表示需要迭代的数据
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    # 如果是迭代器    必须实现iter方法
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index -= 1
            return self.data[self.index]

rev = Reverse([2, 3, 5, 7, 11, 13, 17, 19])
print(next(rev))
print(rev.__next__())
print(isinstance(rev,Iterator))
print(isinstance(rev, Iterable))
print(rev)

for char in rev:
    print(char)
"""
  # 第1步：调用 __iter__() 拿到迭代器
  _iterator = rev.__iter__()      # 等价于 iter(rev)

  # 第2步：无限循环，不停地取下一个值
  while True:
      try:
          char = _iterator.__next__()   # 等价于 next(_iterator)
          # ↓ 这里是你循环体里写的代码
          print(char)
      except StopIteration:
          # 第3步：捕获到停止信号，退出循环
          break
"""

