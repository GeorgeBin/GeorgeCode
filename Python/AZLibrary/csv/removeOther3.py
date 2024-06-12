import csv
import os

# 定义输入根目录
input_root = '/Users/george/Downloads/Downloader/浏览器/Z-Library/处理'

# 定义输入文件路径
input_file = os.path.join(input_root, 'books.csv')

# 定义中间处理文件路径
processed_file = os.path.join(input_root, 'processed_book.csv')

# 定义错误行记录文件路径
error_file = os.path.join(input_root, 'error_lines.csv')

try:
    # 打开输入文件和输出文件
    with open(input_file, 'r', encoding='utf-8') as csv_in, \
            open(processed_file, 'w', newline='', encoding='utf-8') as csv_out, \
            open(error_file, 'w', encoding='utf-8') as error_out:

        # reader = csv.reader(csv_in)
        reader = csv.reader((line.replace('\0','') for line in csv_in),delimiter=",")
        writer = csv.writer(csv_out)
        writerErr = csv.writer(error_out)

        # 读取头部并找到需要的列索引
        header = next(reader)
        print("Header:", header)  # 调试输出
        zlibrary_id_index = None
        extension_index = None
        title_index = None

        for i, col in enumerate(header):
            if col == 'zlibrary_id':
                zlibrary_id_index = i
            elif col == 'extension':
                extension_index = i
            elif col == 'title':
                title_index = i

        # 写入头部
        writer.writerow(['zlibrary_id', 'extension', 'title'])

        # 记录错误的行
        error_lines = []

        # 逐行处理数据并写入新文件
        for row_num, row in enumerate(reader, start=2):
            try:
                if len(row) >= max(zlibrary_id_index, extension_index, title_index) + 1:
                    writer.writerow([row[zlibrary_id_index], row[extension_index], row[title_index]])
                else:
                    writerErr.writerow(row)
            except Exception as e:
                writerErr.writerow(row)

except Exception as e:
    print(f"An error occurred: {e}")

print("完成")

