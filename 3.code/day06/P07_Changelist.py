"""
    通过函数修改列表中元素的练习题
    需求：要函数对列表进行处理，又不希望函数修改原列表
    例如：
        有一个列表，list[1, 2, 3,[100, 200, 300]]
        定义一个函数，向列表中的子列表后追加一个新的元素400===> list[1, 2, 3,[100, 200, 300, 400]]
        但是不希望函数修改原列表，即调用函数后，原列表仍然是[1, 2, 3,[100, 200, 300]]
"""
#%%
import copy

def append_to_sublist(lst):
    # 使用深拷贝，确保不仅复制外层列表，也复制内层的子列表
    new_lst = copy.deepcopy(lst)

    # 假设已知子列表在索引 3 的位置
    new_lst[3].append(400)

    return new_lst

if __name__ == "__main__":
    original_list = [1, 2, 3, [100, 200, 300]]
    result_list = append_to_sublist(original_list)

    print(f"原列表: {original_list}")
    print(f"新列表: {result_list}")

#%%
def change_list(m_list):
    """当前函数演示了deepcopy"""
    print(f"函数内修改列表前列表地址: {id(m_list)}，列表中的元素:{m_list}")
    m_list[3].append(400)
    print(f"函数内修改列表后列表地址: {id(m_list)}，列表中的元素:{m_list}")
list1 = [1, 2, 3,[100, 200, 300]]
print(f"函数外修改列表前列表地址: {id(list1)}，列表中的元素:{list1}")
# 浅拷贝
# list2 = list1.copy()
# 深拷贝
list2 = copy.deepcopy(list1)
print(id(list1[3]))
print(id(list2[3]))
# print(id(list2))
change_list(list2)
print(f"函数外修改列表后列表地址: {id(list1)}，列表中的元素:{list1}")

help(change_list)



