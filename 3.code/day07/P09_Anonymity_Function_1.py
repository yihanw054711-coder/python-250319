"""
    该案例再次对匿名函数进行说明
"""
# list1 要处理的集合
# func  对集合中元素的处理逻辑
my_list = [1, 2, 3, 4, 5]
"""
def my_func(item):
    return item * item

def my_map(list1, func):
    for i, item in enumerate(list1):
        func(item)
        list1[i] = func(item)
    return list1


print(my_map(my_list, my_func))
"""

def my_map(list1, func):
    for i, item in enumerate(list1):
        func(item)
        list1[i] = func(item)
    return list1


print(my_map(my_list, lambda item: item * item))