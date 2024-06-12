import os
import tkinter as tk
from tkinter import filedialog

# 隐藏主窗口
root = tk.Tk()
root.withdraw()

# 选择数据包合并后所在的文件夹
Folderpath = filedialog.askdirectory()
# 选择导出后的txt数据
Filepath = filedialog.askopenfilename()
# 选择输出书本的文件夹
Folderpath2 = filedialog.askdirectory()

# 初始化 allbook 列表
allbook = []

# 打开文件并读取数据
with open(Filepath, "r", encoding='utf-8') as f:
    rubbish = f.readline()  # 读取第一行，直接丢弃。
    lines = f.readlines()  # 读取剩余的所有行

# 处理每一行的数据
for line in lines:
    line = line.strip()  # 去除行尾的换行符
    if line:
        parts = line.split(',')  # 使用逗号分隔
        if len(parts) == 3:
            book = [parts[0], parts[1], parts[2]]  # 分别为编号、扩展名、标题
            allbook.append(book)

# 重命名文件
for i in range(len(allbook)):
    number = allbook[i][0]  # 原来的编号
    newname = allbook[i][0] + "-" +allbook[i][2] + "." + allbook[i][1]  # 新的文件名
    try:
        os.rename(os.path.join(Folderpath, number), os.path.join(Folderpath2, newname))
    except FileNotFoundError:
        print(f"文件 {number} 不存在或出现错误")
    print(f"进度：{i + 1}/{len(allbook)}")

input("转换结束")
