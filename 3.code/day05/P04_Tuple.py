"""
    该案例演示了元组的常用操作
"""
"""
创建元组
"""
# tup = (1, 2, 3)
# 如果元组中只有一个元素，那么在元素的后面也需要加，
# tup1 = (1, )
# print(tup1, type(tup1))
# 使用元组推导式 创建元组
# list1 = [i*2  for i in range(10)]
# print(list1, type(list1))

# tup_gen =(i*2  for i in range(10))
# tup2 = tuple(tup_gen)
# print(tup2, type(tup2))
"""
访问元组中的元素
"""
# tuple1 = (1, 2, 3, 4, 5)
# print(tuple1[-2])
# print(tuple1[0 : -1])

# 元组相加
# tuple1 = (100, 200, 300)
# tuple2 = ("a", "b", "c")
# print(tuple1 + tuple2)

#元组相乘
# tuple1 = (100, 200, 300)
# print(tuple1 * 2)

# 检查成员是否为元组中的元素
# tuple1 = (100, 200, 300)
# print(300 in tuple1)

# 获取元组长度
# tuple1 = (100, 200, 300)
# print(len(tuple1))

# 求元组中元素的最大值、最小值、加和
# tuple1 = (100, 200, 300)
# print(max(tuple1))
# print(min(tuple1))
# print(sum(tuple1))

"""
遍历元组
"""
tuple1 = (100, 200, 300)
# for item in tuple1:
#     print(item)
# for i in range(len(tuple1)):
#     print(tuple1[i])
# for i, item in enumerate(tuple1):
#     print(i, item)

"""
元组不可变
"""
# print(id(tuple1), tuple1)
# tuple1 = tuple1 + (1, 2, 3)
# print(id(tuple1), tuple1)
# 如果元组中元素是可变数据类型，其嵌套项可以被修改。
tuple2 = (100, 200, 300, [1, 2, 3])
print(id(tuple2), tuple2)
tuple2[3].append(4)
print(id(tuple2), tuple2)  # (100, 200, 300, [1, 2, 3, 4])
