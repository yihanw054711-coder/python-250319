"""
    该案例演示了带包模块的导入
"""

"""
# 全局导入
# import graphic.circle 
import graphic.circle as c
print(c.area(5))
"""
"""
# 局部导入  从包中导入模块
from graphic import circle
print(circle.area(5))
"""
"""
# 局部导入 导入包下某个模块的成员
from graphic.circle import area
print(area(5))
"""
"""
# 局部导入 from 包 import *
from graphic import *
print(circle.area(5))
print(retangle(5, 29))
"""
# import graphic.circle
# c = graphic.circle.Circle(59)
# print(c.area())


from graphic import circle, rectangle

c = circle.Circle(59)
r = rectangle.Rectangle(10, 20)
print(c.area())
print(r.area())



