import os

# 所在文件夹
rootPath = "/Users/george/Desktop/test"
directory = rootPath

for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    # 是文件
    if os.path.isfile(file_path):
        try:
            afterName = file[9:]
            print(file_path)
            print(afterName)
            afterPath = directory + "/0" + afterName
            print(afterPath)
            # os.rename(file_path, afterPath) # TODO 会重命名，不要轻易使用
        except Exception as e:  # 未知错误
            print(file_path, e)
    else:
        print(os.path.join(directory, file), "不是文件")
