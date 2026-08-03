"""
    该案例演示set基本操作
"""
""" 
# 创建set集合
set1 = {100, 200, 300}
set2 = set(range(10))
# 注意：如果想声明一个空set，不能用下面的方式，会创建一个空字典
# set3 = {}
set3 = set()
print(set1, type(set1))
print(set2, type(set2))
print(set3, type(set3))
"""
"""
# 添加和删除元素
# {0, 2, 4, 6, 8, 10, 12, 14, 16, 18} <class 'set'>
set1 = {i*2 for i in range(10)}
print(set1, type(set1))
# 向set中添加元素：set.add()，对比list中：list.insert()，list.append(), list.extend()
set1.add(5)
# 向set中删除元素：set.remove()，对比list中：del, list.pop(), list.remove()
# del set1
# print(set1.pop())
set1.remove(5)
"""

# 检查成员是否为集合中的元素
set1 = {1, 2, 3, 4, 5, 6, 7}
print(2 in set1)

# 获取集合长度
set1 = {1, 2, 3, 4, 5}
print(len(set1))  # 5

# 求集合中元素的最大值、最小值、加和
set1 = {1, 2, 3, 4, 5}
print(max(set1))  # 5
print(min(set1))  # 1
print(sum(set1))  # 15

# 5.5.7 遍历集合
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)

