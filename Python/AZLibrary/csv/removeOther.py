import csv

import pandas as pd
import os

# 定义输入根目录
input_root = '/Users/george/Downloads/Downloader/浏览器/Z-Library/处理'

# 定义输入文件路径
input_file = os.path.join(input_root, 'books.csv')

# 定义中间处理文件路径
processed_file = os.path.join(input_root, 'processed_book.csv')

# 打印调试信息
print(f"Input file path: {input_file}")

# 检查文件是否存在
if not os.path.exists(input_file):
    raise FileNotFoundError(f"No such file or directory: '{input_file}'")

# 移除其他列，仅保留3列：zlibrary_id，extension，title
print("Processing the CSV file to keep only the required columns...")

try:
    # 使用 chunksize 参数逐块读取文件，只保留需要的列
    chunksize = 100000  # 每次读取10万行，可以根据实际情况调整
    chunks = []

    for chunk in pd.read_csv(input_file, chunksize=chunksize, usecols=['zlibrary_id', 'extension', 'title'], engine='python', error_bad_lines=False, warn_bad_lines=True, quoting=csv.QUOTE_NONE):
        chunks.append(chunk)

    # 合并所有块，并保存为新的处理文件
    df = pd.concat(chunks)
    df.to_csv(processed_file, index=False)
    print(f"Processed file saved to: {processed_file}")

except pd.errors.ParserError as e:
    print(f"Error parsing file: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
