import csv
import os

# 定义输入根目录
input_root = '/Users/george/Downloads/Downloader/浏览器/Z-Library/处理'

# 定义输入文件路径
input_file = os.path.join(input_root, 'books.csv')

# 定义中间处理文件路径
processed_file = os.path.join(input_root, 'processed_book.csv')

# 定义错误行记录文件路径
error_file = os.path.join(input_root, 'error_lines.txt')

# 打印调试信息
print(f"Input file path: {input_file}")

# 检查文件是否存在
if not os.path.exists(input_file):
    raise FileNotFoundError(f"No such file or directory: '{input_file}'")

# 移除其他列，仅保留3列：zlibrary_id，extension，title
print("Processing the CSV file to keep only the required columns...")

try:
    # 打开输入文件和输出文件
    with open(input_file, 'r', encoding='utf-8') as csv_in, \
            open(processed_file, 'w', newline='', encoding='utf-8') as csv_out, \
            open(error_file, 'w', encoding='utf-8') as error_out:

        reader = csv.reader(csv_in)
        writer = csv.writer(csv_out)

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

        # 如果任何一个索引未找到，引发异常
        if None in [zlibrary_id_index, extension_index, title_index]:
            raise ValueError("Not all required columns found in the header")

        print("Indices:", zlibrary_id_index, extension_index, title_index)  # 调试输出

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
                    print("Skipping row: Insufficient columns")
                    error_lines.append(row_num)
            except Exception as e:
                print(f"Error processing row {row_num}: {e}")
                error_lines.append(row_num)

        # 将错误行写入文件
        if error_lines:
            error_out.write("Error occurred at following row numbers:\n")
            error_out.write('\n'.join(map(str, error_lines)))

    print(f"Processed file saved to: {processed_file}")
    print(f"Error lines saved to: {error_file}")

except Exception as e:
    print(f"An error occurred: {e}")



