"""
    该案例演示了字典基本操作
"""
# dict1 = {}
# dict2 = dict()
# dict3 = {"a":"A", "b":"B", "c":"C"}
# dict4 = dict(a = "A", b = "B", c = "C")
# dict5 = dict([("a", "A"), ("b", "B"), ("c", "C")])
# print(dict1, type(dict1))
# print(dict2, type(dict2))
# print(dict3, type(dict3))
# print(dict4, type(dict4))
# print(dict5, type(dict5))
#
# squares = {x: x**2 for x in range(4)}
# print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9}


# 访问字典元素
# dict1 = {"name": "Alice", "age": 18, "gender": "male"}
# print(dict1["name"])
# print(dict1["age"])
# print(dict1["gender"])
# print(dict1["add"]) # 如果没有对应的键值对，会报错
# print(dict1.get("name"))
# print(dict1.get("age"))
# print(dict1.get("gender"))
# print(dict1.get("add")) # 如果没有对应的键值对，会返回None
# print(dict1.get("add", "earth")) # 如果没有对应的键值对，会返回指定的值

# 向字典中添加元素以及对元素进行修改
# dict1 = {"name": "Alice", "age": 18, "gender": "male"}
# dict1["address"] = "earth"
# dict1["name"] = "Bob"
# print(dict1)
# 判断字典中是否包含某个key
# dict1 = {"name": "Alice", "age": 81, "gender": "male"}
# print("name" in dict1)  # 检查key是否存在
# print("Alice" in dict1)  # 无法直接检查value是否存在
# print(len(dict1))  # 3
"""
# 遍历字典
my_dict = {"name": "Alice", "age": 81, "gender": "male", "address": "earth"}
# 遍历出所有k
# keys = my_dict.keys()
# print(keys, type(my_dict.keys()))
# for k in keys:
#     print (k)
# print("-" *20)
# 遍历出所有v
# vals = my_dict.values()
# print(vals)
# for v in vals:
#     print (v)
# print("-" *20)
# k-v遍历
keys = my_dict.keys()
for k in keys:
    print (k + "---" + str(my_dict[k]))
print("-" *20)

kv = my_dict.items()
for item in kv:
    print(item)
"""


# 删除字典元素
my_dict = {"name": "Alice", "age": 81, "gender": "male", "address": "earth"}
# del my_dict["age"]
# my_dict.clear()
# del my_dict

# dict.pop(key[,default])	获取key所对应的value，同时删除该键值对，可设置默认值
# print(my_dict.pop("age"))
# print(my_dict.pop("country", "unknown"))

# dict.popitem()	取出字典中的最后插入的键值对，字典为空则报错
# print(my_dict.popitem())

# dict1.update(dict2)	将dict2中的键值对更新到dict1中
dict2 = {"language" : "English"}
# my_dict.update(dict2)
# print(my_dict)

# dict.setdefault(key[,default])	获取字典中key对应value，可设置默认值。若key不存在于字典中，将会添加key并将value设为默认值
dict2.setdefault("zr", "aaa")
print(dict2)

# dict.fromkeys(seq[,default])	以序列seq中元素做字典的key创建一个新字典，可设置value的默认值
dict3 = dict.fromkeys(range(5))
print(dict3)


