"""
题目 1：函数定义与调用
定义一个函数 add_numbers，它接受两个整数参数 a 和 b，返回这两个数的和，并调用该函数计算 3 和 5 的和。
"""
def add_numbers(a, b):
    result = a + b
    return result
print(add_numbers(3,5))

"""
题目 2：默认参数
定义一个函数 greet，它接受一个字符串参数 name，并且有一个默认参数 message，默认值为 “Hello”，函数功能是打印出问候语，如 “Hello, Alice”。调用该函数时，分别传入和不传入 message 参数进行测试。
"""
def greet(name, message = "Hello"):
    print(f"{message}, {name}")
greet("Alice")
greet("Alice", "Goodbye")

"""
题目 3：可变参数
定义一个函数 sum_all，它接受任意数量的整数参数，返回所有参数的和。例如调用 sum_all(1, 2, 3) 应返回 6，调用 sum_all(10, 20, 30, 40) 应返回 100。
"""
def sum_all(*args):
    result = sum(args)
    return result
print(sum_all(1, 2, 3))
print(sum_all(10, 20, 30, 40))

"""
题目 4：函数嵌套调用
定义两个函数，square 函数接受一个整数参数，返回该数的平方；cube 函数接受一个整数参数，通过调用 square 函数返回该数的立方（立方 = 平方 × 该数）。调用 cube 函数计算 3 的立方。
"""
def square(num):
    return num ** 2
def cube(num):
    return num * square(num)
print(cube(3))

"""
编程题 1：数字反转
编写一个函数，接受一个整数作为参数，返回该整数的反转形式。例如，输入 123，返回 321；输入 -456，返回 -654。
"""
# def reverse(num):
#     num = str(num)
#     return num[::-1]

# def reverse(num):
#     res = 0
#     while num > 0:
#         res = res * 10 + num % 10   # 每次取最后一位，拼到结果末尾
#         num //= 10                   # 去掉最后一位
#     return res

def reverse(num):
    c = 0
    while num > 0:
        a = num % 10
        num = num // 10
        c = c * 10 + a
    return c
print(reverse(123))
"""
编程题 2：嵌套字典数据处理
有一个嵌套字典，存储了学生的课程成绩信息。 编写一个函数，计算每个学生的平均成绩，并返回一个新的字典，键为学生名字，值为平均成绩。
结构如下：
students = {
    "Alice": {
        "Math": 85,
        "English": 90,
        "Science": 78
    },
    "Bob": {
        "Math": 92,
        "English": 88,
        "Science": 95
    },
    "Charlie": {
        "Math": 70,
        "English": 75,
        "Science": 80
    }
}
"""
students = {
    "Alice": {
        "Math": 85,
        "English": 90,
        "Science": 78
    },
    "Bob": {
        "Math": 92,
        "English": 88,
        "Science": 95
    },
    "Charlie": {
        "Math": 70,
        "English": 75,
        "Science": 80
    }
}

def calculate_average_grades(students):
    """
    Calculate each student's average grade from a nested dictionary.

    Args:
        students (dict): Nested dict structured as:
            {"StudentName": {"CourseName": grade, ...}, ...}

    Returns:
        dict: {"StudentName": average_grade (float), ...}
    """
    result = {}
    for student, grades in students.items():
        total = sum(grades.values())
        average = total / len(grades)
        result[student] = average
    return result
print(calculate_average_grades(students))

