"""
    该案例演示了字符串常用的函数
"""
"""
str.replace(old,new[,max])	
把将字符串中的old替换成new,如果指定max，则替换不超过max次
"""
# str1 = "hello world"
# str2 = str1.replace("o", "a", 2)
# print(str1)
# print(str2)
# str1 = "hello world"

# result = []
# count = 0
# for ch in str1:
#     if ch == "o" and count < 2:
#         result.append("a")
#         count += 1
#     else:
#         result.append(ch)
#
# str2 = "".join(result)
# print(str2)

"""
str.split([x][,n])	
按x分隔字符串，并且以list的形式输出，默认按任何空白字符串分隔并在结果中丢弃空字符串。可指定最大分隔次数
"""
str1 = "a, b, c, d, e, f"
print(type(str1.split(", ")))
print(str1.split(", ", 2))

"""
x.join(seq)	
以x作为分隔符，将列表序列中所有的字符串合并为一个新的字符串
"""
list1 = ["a", "b", "c", "d", "e", "f"]
# 列表中的元素类型，必须得是字符串
str1 = "-".join(list1)
print(str1)
"""
str.find(x[,start][,end])	
返回字符串中第一个x的索引值，不存在则返回-1，可指定字符串开始结束范围
"""
str1 = "dhaadhahihdfcjska"
print(str1.find("a", 2, 15))
"""
str.index(x[,start][,end])	
返回字符串中第一个x的索引值，不存在则报错，可指定字符串开始结束范围
"""
str1 = "dhaadhahihdfcjska"
print(str1.index("aad", 2, 10))