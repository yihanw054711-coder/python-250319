"""
    该案例演示了文件的拷贝
"""

# 优化：一次不要读取全部文件内容
def file_copy(source_file_path, dest_file_path):
    # 打开源文件
    source_file = open(source_file_path, "rb")
    # 打开目标文件
    dest_file = open(dest_file_path, "wb")

    # 从源文件中读取数据
    content = source_file.read(1024)

    # 将读取到的数据写入目标文件
    while content:
        dest_file.write(content)
        content = source_file.read(1024)

    # 关闭源文件
    source_file.close()

    # 关闭目标文件
    dest_file.close()

file_copy("/Users/wyh/Pictures/已粘贴 2026-06-30 上午9.33.44.png", "/Users/wyh/dev/workspace/python-250319/day08/上午9.33.44.png")
