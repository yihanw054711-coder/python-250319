"""
题目 1：函数嵌套调用
定义两个函数，square 函数接受一个整数参数，返回该数的平方；
cube 函数接受一个整数参数，通过调用 square 函数返回该数的立方（立方 = 平方 × 该数）。
调用 cube 函数计算 3 的立方。
"""
def square(num):
    return num * num
def cube(num):
    return num * square(num)
print(cube(3))


"""
题目2：文件操作 - 写入和读取文件
1.编写代码创建一个新的文本文件 output.txt，并向其中写入字符串 “This is a test.”。
2.读取该文件的内容并打印出来
"""
f = open("output.txt", "w")
f.write("This is a test.")
f.close()

f = open("output.txt", "r")
print(f.read())