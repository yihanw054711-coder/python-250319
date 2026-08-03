"""
    该案例演示了浅拷贝与深拷贝
"""
import copy
"""
# 浅拷贝   [:] list()  copy()
list1 = [1000, 2,3, [100, 200, 300]]
list2= list1.copy()
list3= copy.deepcopy(list1)
# 对list1中不可变数据类型进行修改
list1[0] = 10
# 对list1中可变数据类型进行修改
list1[3].append(400)
print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)
print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)
print(id(list3), id(list3[0]), id(list3[1]), id(list3[2]), id(list3[3]), list3)
"""
# 拷贝的特殊情况
# （1）非容器类型（如数字、字符串、和其他“原子”类型的对象）无法拷贝
var1 = 1
var2 = copy.copy(var1)
var3 = copy.deepcopy(var1)
var1 = 10
print(id(var1), var1)  # 140732039489976 1
print(id(var2), var2)  # 140732039489976 1
print(id(var3), var3)  # 140732039489976 1
#（2）元组变量如果只包含原子类型对象，则不能对其深拷贝
tuple1 = (1, 2, 3)  # 元组只包含原子类型对象
print(id(tuple1), tuple1)  # 1653947230848 (1, 2, 3)

tuple2 = copy.deepcopy(tuple1)
print(id(tuple2), tuple2)  # 1653947230848 (1, 2, 3)

tuple1 = (1, 2, 3, [])  # 元组不只包含原子类型对象
print(id(tuple1), tuple1)  # 1653947152432 (1, 2, 3, [])

tuple2 = copy.deepcopy(tuple1)
print(id(tuple2), tuple2)  # 1653947148912 (1, 2, 3, [])





