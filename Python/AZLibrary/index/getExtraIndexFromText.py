import os
import csv


def load_index_files(index_folder):
    """加载 index 文件夹内的所有 .txt CSV 文件，返回一个字典，键为 zlibrary_id，值为 (extension, title)"""
    index_data = {}

    # 遍历 index 文件夹内的所有 .txt 文件
    for file_name in os.listdir(index_folder):
        if file_name.endswith(".txt"):
            file_path = os.path.join(index_folder, file_name)
            with open(file_path, 'r', encoding='utf-8') as f:
                # 使用制表符作为分隔符，读取 CSV 文件
                reader = csv.DictReader(f, delimiter='\t', quotechar='"')
                for row in reader:
                    zlibrary_id = row['zlibrary_id']
                    extension = row['extension']
                    title = row['title']
                    index_data[zlibrary_id] = (extension, title)

    return index_data


def load_ids(file_path):
    """加载 a.txt 文件中的 id 列表"""
    ids = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t', quotechar='"')
        next(reader)  # 跳过表头
        for row in reader:
            id = row[0]
            if id:
                ids.append(id)
    return ids


def write_output(matched_data, output_file):
    """将匹配的结果写入 output.txt 文件"""
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        # 创建csv.writer对象，确保用制表符分隔，并且字段带有引号
        writer = csv.writer(f, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
        # 写入表头，字段用引号包裹
        writer.writerow(['zlibrary_id', 'extension', 'title'])
        # 写入匹配到的数据
        for zlibrary_id, (extension, title) in matched_data.items():
            writer.writerow([zlibrary_id, extension, title])


def main():
    # 指定 index 文件夹路径
    index_folder = '~/AZLibrary/index/index-zlib1'  # 确保这个文件夹包含所有的 index.txt 文件
    # 加载 temp.txt 文件的路径
    a_file_path = '~/AZLibrary/temp.txt'
    # 定义输出文件路径
    output_file = '~/AZLibrary/index/index-zlib2/pilimi-zlib2-0-14679999-extra（总：16156）.txt'

    # 加载 index 文件的数据
    index_data = load_index_files(index_folder)

    # 加载 temp.txt 文件中的 id
    ids = load_ids(a_file_path)

    # 匹配的结果
    matched_data = {}

    # 根据 id 匹配 zlibrary_id
    for id in ids:
        if id in index_data:
            matched_data[id] = index_data[id]
        else:
            print(f'ID {id} 未在 index 文件中找到')

    # 将匹配结果写入 output.txt
    write_output(matched_data, output_file)
    print(f"输出文件已生成：{output_file}")


if __name__ == "__main__":
    main()
