import os
import csv
import tkinter as tk
from tkinter import filedialog
import re
from pathvalidate import sanitize_filename

# 隐藏主窗口
root = tk.Tk()
root.withdraw()

# 选择数据包合并后所在的文件夹
# Folderpath = filedialog.askdirectory()
# # 选择导出后的txt数据
# Filepath = filedialog.askopenfilename()
# # 选择输出书本的文件夹
# Folderpath2 = filedialog.askdirectory()

# 读取CSV文件并保留所需的列
input_root = '/Users/george/Downloads/Downloader/浏览器/Z-Library/其他/测试数据2'
# 定义输入文件路径
Folderpath = os.path.join(input_root, '下载文件')
# 定义错误文件路径
Filepath = os.path.join(input_root, '索引/pilimi-zlib-0-119999.csv')
Folderpath2 = os.path.join(input_root, '修改后文件')

# 初始化 allbook 列表
allbook = []

# 打开文件并读取数据
with open(Filepath, "r", encoding='utf-8') as f:
    rubbish = f.readline()  # 读取第一行，直接丢弃。
    lines = f.readlines()  # 读取剩余的所有行

# 定义错误文件路径
error_file = os.path.join(Folderpath2, 'rename_err.csv')

# 打开输入文件和错误文件
with open(error_file, 'w', newline='') as errfile:
    writer_err = csv.writer(errfile)
    writer_err.writerow(['zlibrary_id', 'extension', 'title'])

    # 处理每一行的数据
    for line in lines:
        line = line.strip()  # 去除行尾的换行符
        if line:
            parts = line.split(',')  # 使用逗号分隔
            if len(parts) == 3:
                book = [parts[0], parts[1], parts[2]]  # 分别为编号、扩展名、标题
                allbook.append(book)

    # 重命名文件
    for i, book in enumerate(allbook, start=1):
        number, extension, title = book

        try:
            old_path = os.path.join(Folderpath, number)
            if os.path.exists(old_path):

                newname = f"{number}-{title}.{extension}"
                # newname = re.sub(r'[\\/:"*?<>|]+', '', newname)  # 移除非法字符
                newname = sanitize_filename(newname)  # 移除非法字符

                new_path = os.path.join(Folderpath2, newname)
                os.rename(old_path, new_path)
            else:
                # 文件不存在，记录到错误文件中
                writer_err.writerow(book)
        except Exception as e:
            writer_err.writerow(book)
            print(f"An error occurred: {e}")
        print(f"进度：{i}/{len(allbook)}")

input("转换结束")
