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
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        next(f)  # 跳过表头行
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) != len(header_names):
                print(f"Skipping malformed line: {line.strip()}")
                continue
            row_data = {header_names[i]: fields[i].strip('"') for i in range(len(header_names))}
            data.append(row_data)
    return data


# 隐藏主窗口
root = tk.Tk()
root.withdraw()

Folderpath = filedialog.askdirectory()  # 下载文件所在目录
Filepath = filedialog.askopenfilename()  # 索引文件
Folderpath2 = filedialog.askdirectory()  # 重命名后文件输出目录
#
# todo：根目录
# input_root = '/Users/george/Downloads/Downloader/浏览器/Z-Library/Test/Demo'
# Folderpath = os.path.join(input_root, '下载文件')  # 下载文件所在目录
# Filepath = os.path.join(input_root, 'index.txt')  # 索引文件
# Folderpath2 = os.path.join(input_root, '修改后文件')  # 重命名后文件输出目录


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
            print(f"重命名发生错误：{e}")
            try:
                writer_err.writerow([book, str(e)])  # 记录错误信息到错误文件中
            except Exception as e2:
                print(f"写错误到文件发生错误：{e2}")

        if i % 1000 == 0:
            print(f"进度：{i}/{len(allbook)}")  # 每 1000 条输出一次进度日志

input("转换结束")
# root.destroy()
