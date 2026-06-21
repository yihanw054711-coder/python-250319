"""
    每日一考
"""

"""
题目 1：集合操作
现有集合 set1 = {1, 2, 3, 4, 5} 和 set2 = {3, 4, 5, 6, 7} 。
求这两个集合的并集。
求这两个集合的交集。
从 set1 中移除元素 3 。
"""
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print(set1 | set2)
print(set1 & set2)
set1.remove(3)
print(set1)

"""
题目 2：字典操作
有字典 person = {‘name’: ‘Alice’, ‘age’: 25, ‘city’: ‘New York’} 。
获取字典中 ‘age’ 对应的值。
向字典中添加一个键值对 ‘job’: ‘Engineer’ 。
删除字典中 ‘city’ 这个键值对。
"""
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person["age"])
person["job"] = "Engineer"
del person["city"]
print(person)

"""
题目 3：集合与字典综合
创建一个集合，包含数字 1 到 5 。再创建一个字典，键为集合中的数字，值为该数字的平方。
"""
set ={1, 2, 3, 4,5}
dict1 = {i:i**2 for i in set}
print(dict1)

# 拓展题目
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]
dict2 = {k:v for k , v in zip(list1, list2)}
print(dict2)
dict3 = dict(zip(list1, list2))
print(dict3)
# 标准错误写法
dic4 = {k:v for k in list1 for v in list2}
print(dic4) # {1: 'e', 2: 'e', 3: 'e', 4: 'e', 5: 'e'}

