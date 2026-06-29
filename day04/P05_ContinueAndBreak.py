"""
    该案例演示了continue和break关键词
"""
# 案例：打印0-9，跳过偶数。
# for i in range(10):
#     # 判断i是否是偶数
#     if i % 2 == 0:
#         # 跳出当前正在进行的本次循环，继续下一次循环
#         continue
#     print(i)

# break关键字
# i = 0
# for i in range(10):
#     # 判断i是否是偶数
#     if i % 2 == 0:
#         # 跳出当前循环，结束循环
#         break
#     print(i)
# print("end")

# 案例：求0-9每个数自己幂自己的加和，如果大于10000000则循环终止。
sum = 0
for i in range(10 ):
    # 幂运算
    sum += i ** i
    # 判断是否大于10000000
    if sum > 10000000:
        # 跳出当前循环，结束循环
        break
    print(i, sum)
else:
    print("循环正常结束")

# pass关键字
# while True:
#     pass

# 循环 + else（一般和break配合使用）
# target = 3
# for i in [1, 2, 3, 4, 5]:
#     if i == target:
#         print(f"当前要查找的值{target}在列表中")
#         break
# else:
#     print("在当前列表中没有找到目标元素")