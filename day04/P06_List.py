"""
    该案例演示了列表相关操作
"""
# 创建新的列表
list1 = [100, 200, 300, 400, 500]
# print(list1)
# print(type(list1))
# 通过索引获取列表中的元素
# print(list1[1])
# 列表切片
# 复制整个列表
# list2 = list1[0:len(list1)]
# print(list1[0:len(list1)])
# print(id(list1), id(list2))
# print(list1 is list2)
# 复制整个列表
# print(list1[:])
# # 取索引从2开始到4(不包含)的元素
# print(list1[2:4])
# # 取索引从2开始到末尾的元素
# print(list1[2:])
# # 取索引从0开始到2(不包含)的元素
# print(list1[:2])
# # 取索引从2开始到-1(不包含)的元素
# print(list1[2:-1])
# 倒序取元素
# print(list1[::-1])
# print(list1[3:2:-1])

# 向列表中添加元素：insert方法以及append方法
# print(list1.insert(3, 800))
"""
返回的是NONE，说明该方法没有返回值，直接修改了原列表
"""
# 在指定的索引位置添加元素（地址不变，内容改变）
# list1.insert(3, 800)
# 在列表的末尾添加元素
# list1.append(800)

# 列表相加
# list1 = [1,2,3]
# list2 = ["a", "b", "c"]
# print((list1 + list2))


# 列表相乘
# print(list1 * 3)

# 修改列表元素-通过下标修改
# list1[2] = "a"
# print(list1)
# 修改列表元素-通过切片修改
# list1[1:3] = ["a", "b", "c"]
# print(list1)

# 判断成员是否为列表元素
# print(300 in list1)

# 获取列表长度
# print(len(list1))
# 求列表中元素的最大值、最小值、加和
# list1.append(200)
# print(max(list1))
# print(min(list1))
# print(sum(list1))

# 列表元素的遍历（3种方法）
# 方法1、直接对列表进行遍历
# for item in list1:
#     print(item)

# 方法2、通过下标获取列表中的元素
# list[下标]
# 循环次数：len(list1)
# for循环，先生成一个序列，起始值要和下标对应，从0开始
# for i in range(0,len(list1)):
#     print(i, list1[i])
# while循环，先生成一个序列，起始值要和下标对应，从0开始
# i = 0
# while i < len(list1):
#     print(i, list1[i])
#     i += 1

# 方法3、通过enumerate函数直接遍历出下标和值（该函数返回元组）
# print(id(enumerate(list1)))
# print(enumerate(list1))
# for i, item in enumerate(list1):
#     print(i, item)

# 从列表中删除元素
# 通过del语句删除列表中的元素
# del list1[2]

# list1.insert(3,300)
# list1.remove(300)   # 删除第一次出现的x

# list1.pop(3)
# print(list1)

# list2 = [100, 200, 300, [500, 600, 700], 400]
# print(list2[3])

# 列表推导式 在已经存在可迭代对象的基础上，通过运算或者过滤，得到新的列表
# 基础列表推导式
# squares = [x**2 for x in range(5)]
# print(squares)
# 带条件的列表推导式
# squares = [x**2 for x in range(10) if x % 2 == 0]
# print(squares)
# 使用现有列表的列表推导式
# list1 = [100, 200, 300, 400, 500]
# squares = [x**2 for x in list1]
# print(squares)
# 包含多个循环的列表推导式
# list1 = [1, 2, 3, 4, 5]
# list2 = ["a", "b", "c", "d", "e"]
# tuple_list = [(i, j) for i in list1 for j in list2]
# print(tuple_list)


# zip函数  拉链函数
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = ["a", "b", "c", "d", "e"]
zipped = zip(list1, list2)
print(zipped)
print(type(zipped))
print(list(zipped))
for item in zipped:
    print(item)







