"""
    该案录演示了读写文件操作
"""
"""
# 向文件中写入数据
# 打开文件（建立程序和文件之间的通道）
f = open("test.txt","w")

# 向文件中写入数据
f.write("hello world\n")
f.write("nihao python\n")

# 关闭和文件之间建立的通道
f.close()
"""
"""
# 从文件中读取数据
# 打开文件（建立程序和文件之间的通道）
f = open("test.txt","r")
# 从文件中读取数据  read()默认读取所有数据，也可以读取指定的字节数大小数据
print(f.read(5))
print(f.read(8))

# 关闭和文件之间建立的通道
f.close()
"""
# 读取一行数据
# f = open("test.txt","r")
# print(f.readline())
# print(f.readline())
# f.close()
# 读取所有行
f = open("test.txt","r")
print(f.readlines())
f.close()