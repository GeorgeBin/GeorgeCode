
import pandas as pd
import os

# 定义分割范围和对应文件名
ranges = [
    (0, 119999, 'pilimi-zlib-0-119999.csv'),
    (120000, 419999, 'pilimi-zlib-120000-419999.csv'),
    (420000, 2379999, 'pilimi-zlib-420000-2379999.csv'),
    (2380000, 2829999, 'pilimi-zlib-2380000-2829999.csv'),
    (2830000, 5239999, 'pilimi-zlib-2830000-5239999.csv'),
    (5240000, 5329999, 'pilimi-zlib-5240000-5329999.csv'),
    (5330000, 5359999, 'pilimi-zlib-5330000-5359999.csv'),
    (5360000, 5379999, 'pilimi-zlib-5360000-5379999.csv'),
    (5380000, 5449999, 'pilimi-zlib-5380000-5449999.csv'),
    (5450000, 5479999, 'pilimi-zlib-5450000-5479999.csv'),
    (5480000, 5499999, 'pilimi-zlib-5480000-5499999.csv'),
    (5500000, 5519999, 'pilimi-zlib-5500000-5519999.csv'),
    (5520000, 5549999, 'pilimi-zlib-5520000-5549999.csv'),
    (5550000, 5579999, 'pilimi-zlib-5550000-5579999.csv'),
    (5580000, 5609999, 'pilimi-zlib-5580000-5609999.csv'),
    (5610000, 5639999, 'pilimi-zlib-5610000-5639999.csv'),
    (5640000, 5659999, 'pilimi-zlib-5640000-5659999.csv'),
    (5660000, 5709999, 'pilimi-zlib-5660000-5709999.csv'),
    (5710000, 5729999, 'pilimi-zlib-5710000-5729999.csv'),
    (5730000, 5749999, 'pilimi-zlib-5730000-5749999.csv'),
    (5750000, 5769999, 'pilimi-zlib-5750000-5769999.csv'),
    (5770000, 5789999, 'pilimi-zlib-5770000-5789999.csv'),
    (5790000, 5809999, 'pilimi-zlib-5790000-5809999.csv'),
    (5810000, 6039999, 'pilimi-zlib-5810000-6039999.csv'),
    (6040000, 6069999, 'pilimi-zlib-6040000-6069999.csv'),
    (6070000, 6129999, 'pilimi-zlib-6070000-6129999.csv'),
    (6130000, 6159999, 'pilimi-zlib-6130000-6159999.csv'),
    (6160000, 7229999, 'pilimi-zlib-6160000-7229999.csv'),
    (7230000, 9459999, 'pilimi-zlib-7230000-9459999.csv'),
    (9460000, 10999999, 'pilimi-zlib-9460000-10999999.csv'),
    (11000000, 11039999, 'pilimi-zlib-11000000-11039999.csv'),
    (11040000, 11079999, 'pilimi-zlib-11040000-11079999.csv'),
    (11080000, 11129999, 'pilimi-zlib-11080000-11129999.csv'),
    (11130000, 11169999, 'pilimi-zlib-11130000-11169999.csv'),
    (11170000, 11209999, 'pilimi-zlib-11170000-11209999.csv'),
    (11210000, 11269999, 'pilimi-zlib-11210000-11269999.csv'),
    (11270000, 11299999, 'pilimi-zlib-11270000-11299999.csv'),
    (11300000, 11329999, 'pilimi-zlib-11300000-11329999.csv'),
    (11330000, 11359999, 'pilimi-zlib-11330000-11359999.csv'),
    (11360000, 11399999, 'pilimi-zlib-11360000-11399999.csv'),
    (11400000, 11449999, 'pilimi-zlib-11400000-11449999.csv'),
    (11450000, 11499999, 'pilimi-zlib-11450000-11499999.csv'),
    (11500000, 11549999, 'pilimi-zlib-11500000-11549999.csv'),
    (11550000, 11579999, 'pilimi-zlib-11550000-11579999.csv'),
    (11580000, 11599999, 'pilimi-zlib-11580000-11599999.csv'),
    (11600000, 11659999, 'pilimi-zlib-11600000-11659999.csv'),
    (11660000, 11699999, 'pilimi-zlib-11660000-11699999.csv'),
    (11700000, 11729999, 'pilimi-zlib-11700000-11729999.csv'),
    (11730000, 11759999, 'pilimi-zlib-11730000-11759999.csv'),
    (11760000, 11799999, 'pilimi-zlib-11760000-11799999.csv'),
    (11800000, 11829999, 'pilimi-zlib-11800000-11829999.csv'),
    (11830000, 11859999, 'pilimi-zlib-11830000-11859999.csv'),
    (11860000, 11899999, 'pilimi-zlib-11860000-11899999.csv'),
    (11900000, 11929999, 'pilimi-zlib-11900000-11929999.csv'),
    (11930000, 11949999, 'pilimi-zlib-11930000-11949999.csv'),
    (11950000, 11969999, 'pilimi-zlib-11950000-11969999.csv'),
    (11970000, 11999999, 'pilimi-zlib-11970000-11999999.csv'),
    (12000000, 12039999, 'pilimi-zlib-12000000-12039999.csv'),
    (12040000, 12099999, 'pilimi-zlib-12040000-12099999.csv'),
    (12100000, 12159999, 'pilimi-zlib-12100000-12159999.csv'),
    (12160000, 12229999, 'pilimi-zlib-12160000-12229999.csv'),
    (12230000, 12349999, 'pilimi-zlib-12230000-12349999.csv'),
    (12350000, 12619999, 'pilimi-zlib-12350000-12619999.csv'),
    (12620000, 12769999, 'pilimi-zlib-12620000-12769999.csv'),
    (12770000, 12809999, 'pilimi-zlib-12770000-12809999.csv'),
    (12810000, 13229999, 'pilimi-zlib-12810000-13229999.csv'),
    (13230000, 13529999, 'pilimi-zlib-13230000-13529999.csv'),
    (13530000, 13849999, 'pilimi-zlib-13530000-13849999.csv'),
    (13850000, 13959999, 'pilimi-zlib-13850000-13959999.csv'),
    (13960000, 14029999, 'pilimi-zlib-13960000-14029999.csv'),
    (14030000, 14379999, 'pilimi-zlib-14030000-14379999.csv'),
    (14380000, 14679999, 'pilimi-zlib-14380000-14679999.csv'),
    (14680000, 14999999, 'pilimi-zlib2-14680000-14999999.csv'),
    (15000000, 15679999, 'pilimi-zlib2-15000000-15679999.csv'),
    (15680000, 16179999, 'pilimi-zlib2-15680000-16179999.csv'),
    (16180000, 16379999, 'pilimi-zlib2-16180000-16379999.csv'),
    (16380000, 16469999, 'pilimi-zlib2-16380000-16469999.csv'),
    (16470000, 16579999, 'pilimi-zlib2-16470000-16579999.csv'),
    (16580000, 16679999, 'pilimi-zlib2-16580000-16679999.csv'),
    (16680000, 16779999, 'pilimi-zlib2-16680000-16779999.csv'),
    (16780000, 16829999, 'pilimi-zlib2-16780000-16829999.csv'),
    (16830000, 16869999, 'pilimi-zlib2-16830000-16869999.csv'),
    (16870000, 16939999, 'pilimi-zlib2-16870000-16939999.csv'),
    (16940000, 17059999, 'pilimi-zlib2-16940000-17059999.csv'),
    (17060000, 17179999, 'pilimi-zlib2-17060000-17179999.csv'),
    (17180000, 17289999, 'pilimi-zlib2-17180000-17289999.csv'),
    (17290000, 17399999, 'pilimi-zlib2-17290000-17399999.csv'),
    (17400000, 17509999, 'pilimi-zlib2-17400000-17509999.csv'),
    (17510000, 17609999, 'pilimi-zlib2-17510000-17609999.csv'),
    (17610000, 17669999, 'pilimi-zlib2-17610000-17669999.csv'),
    (17670000, 17729999, 'pilimi-zlib2-17670000-17729999.csv'),
    (17730000, 17809999, 'pilimi-zlib2-17730000-17809999.csv'),
    (17810000, 17899999, 'pilimi-zlib2-17810000-17899999.csv'),
    (17900000, 17999999, 'pilimi-zlib2-17900000-17999999.csv'),
    (18000000, 18219999, 'pilimi-zlib2-18000000-18219999.csv'),
    (18220000, 18269999, 'pilimi-zlib2-18220000-18269999.csv'),
    (18270000, 18329999, 'pilimi-zlib2-18270000-18329999.csv'),
    (18330000, 18399999, 'pilimi-zlib2-18330000-18399999.csv'),
    (18400000, 18469999, 'pilimi-zlib2-18400000-18469999.csv'),
    (18470000, 18599999, 'pilimi-zlib2-18470000-18599999.csv'),
    (18600000, 18799999, 'pilimi-zlib2-18600000-18799999.csv'),
    (18800000, 18879999, 'pilimi-zlib2-18800000-18879999.csv'),
    (18880000, 18959999, 'pilimi-zlib2-18880000-18959999.csv'),
    (18960000, 19039999, 'pilimi-zlib2-18960000-19039999.csv'),
    (19040000, 19139999, 'pilimi-zlib2-19040000-19139999.csv'),
    (19140000, 19209999, 'pilimi-zlib2-19140000-19209999.csv'),
    (19210000, 19299999, 'pilimi-zlib2-19210000-19299999.csv'),
    (19300000, 19439999, 'pilimi-zlib2-19300000-19439999.csv'),
    (19440000, 19559999, 'pilimi-zlib2-19440000-19559999.csv'),
    (19560000, 19719999, 'pilimi-zlib2-19560000-19719999.csv'),
    (19720000, 19819999, 'pilimi-zlib2-19720000-19819999.csv'),
    (19820000, 19919999, 'pilimi-zlib2-19820000-19919999.csv'),
    (19920000, 19999999, 'pilimi-zlib2-19920000-19999999.csv')
]

# 读取CSV文件并保留所需的列
input_root = '/Users/george/Downloads/Downloader/浏览器/Z-Library/处理'
# 定义输入文件路径
input_file = os.path.join(input_root, 'processed_book.csv')
# 定义错误文件路径
error_file = os.path.join(input_root, 'err.csv')


# 使用 chunksize 参数逐块读取文件
chunksize = 100000  # 每次读取10万行，可以根据实际情况调整

# 初始化一个空的 DataFrame 字典
dfs = {range_tuple[2]: pd.DataFrame() for range_tuple in ranges}

# 逐块读取文件并处理
try:
    with open(error_file, 'w') as err_csv:
        err_csv.write("zlibrary_id,extension,title\n")
        for chunk in pd.read_csv(input_file, chunksize=chunksize, usecols=['zlibrary_id', 'extension', 'title'],
                                 engine='python', error_bad_lines=False, warn_bad_lines=True):
            # 将 zlibrary_id 列转换为整数类型，并捕获转换失败的异常
            try:
                chunk['zlibrary_id'] = chunk['zlibrary_id'].astype(int)
            except ValueError:
                chunk[~chunk['zlibrary_id'].astype(str).str.isdigit()].to_csv(err_csv, index=False, header=False)
                continue

            for start, end, filename in ranges:
                mask = (chunk['zlibrary_id'] >= start) & (chunk['zlibrary_id'] <= end)
                if not mask.any():
                    continue
                dfs[filename] = pd.concat([dfs[filename], chunk.loc[mask]])

    # 保存到不同的 CSV 文件中
    for filename, df in dfs.items():
        if not df.empty:
            output_file = os.path.join(input_root, filename)
            df.to_csv(output_file, index=False)

    print("分割完成")
except pd.errors.ParserError as e:
    print(f"Error parsing file: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

print("所有文件处理完成。")
