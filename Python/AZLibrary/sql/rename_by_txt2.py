import os
import csv
import tkinter as tk
from tkinter import filedialog
import re
from pathvalidate import sanitize_filename

# 列名
header_names = ['zlibrary_id', 'extension', 'title']
MAX_FILENAME_LENGTH = 250


def parse_txt_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        next(f)  # 跳过表头行
        data = []
        for line in f:
            # 将每一行数据拆分为字段
            fields = line.strip().split('\t')
            row_data = {}  # 创建一个字典来存储每个字段
            for i, field in enumerate(fields):
                # 使用列名作为键
                row_data[header_names[i]] = field.strip('"')
            # 将字典添加到列表中
            data.append(row_data)
            # print(f"row_data：{row_data}")
    return data


# 隐藏主窗口
root = tk.Tk()
root.withdraw()

# # todo：根目录
# input_root = '/Users/george/Downloads/Downloader/浏览器/Z-Library/Test/3. 使用 SQL 导出数据'
# Folderpath = os.path.join(input_root, '下载文件')  # 下载文件所在目录
# Filepath = os.path.join(input_root, 'pilimi-zlib-0-10（总 10）.txt')  # 索引文件
# Folderpath2 = os.path.join(input_root, '修改后文件')  # 重命名后文件输出目录


Folderpath = filedialog.askdirectory()  # 下载文件所在目录
Filepath = filedialog.askopenfilename()  # 索引文件
Folderpath2 = filedialog.askdirectory()  # 重命名后文件输出目录

error_file = os.path.join(Folderpath2, 'rename_err.txt')  # 定义输出日志路径：发生错误
no_file = os.path.join(Folderpath2, 'rename_no.txt')  # 定义输出日志路径：没有找到文件

allbook = parse_txt_file(Filepath)

# 打开输入文件和错误文件
with open(error_file, 'w', newline='', encoding='utf-8') as errorfile, open(no_file, 'w', newline='', encoding='utf-8') as nofile:
    writer_err = csv.writer(errorfile)
    writer_err.writerow(['zlibrary_id', 'extension', 'title', 'err'])
    writer_no = csv.writer(nofile)
    writer_no.writerow(['zlibrary_id', 'extension', 'title'])

    # 重命名文件
    for i, book in enumerate(allbook, start=1):
        try:
            # number, extension, title = book
            zlibrary_id = book["zlibrary_id"]
            extension = book["extension"]
            title = book["title"]

            # print(f"zlibrary_id={zlibrary_id}")
            # print(f"extension={extension}")
            # print(f"title={title}")
            # print(f"book={book}")

            old_path = os.path.join(Folderpath, zlibrary_id)
            if os.path.exists(old_path):

                max_title_length = MAX_FILENAME_LENGTH - len(zlibrary_id) - len(extension) - 3

                if len(title) > max_title_length:
                    truncated_title = title[:max_title_length]
                else:
                    truncated_title = title

                newname = f"{zlibrary_id}-{truncated_title}.{extension}"
                newname2 = sanitize_filename(newname)  # 移除非法字符-->如果长度超标，可能会造成后缀丢失
                new_path = os.path.join(Folderpath2, newname2)
                os.rename(old_path, new_path)
                # print(f"文件存在：{zlibrary_id}")
            else:
                writer_no.writerow([book['zlibrary_id'], book['extension'], book['title']])  # 文件不存在，记录到错误文件中
                print(f"文件不存在：{zlibrary_id}")
        except Exception as e:
            # writer_err.writerow([book['zlibrary_id'], book['extension'], book['title'], e])  # 报错，记录到错误文件中
            print(f"An error occurred: {e}")

        print(f"进度：{i}/{len(allbook)}")

input("转换结束")
# root.destroy()
