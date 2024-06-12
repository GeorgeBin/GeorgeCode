import piexif
import os
import shutil
from datetime import datetime


def makeFile(path):
    print(f'makeFile, {path}')  # Press ⌘F8 to toggle the breakpoint.
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return False


# 照片所在文件夹
rootPath = "/Users/george/Desktop/Test"

directory = rootPath

# 没有处理的文件
invalid = rootPath + "/invalid"
gif = rootPath + "/gif"
png = rootPath + "/png"
other = rootPath + "/other"

makeFile(invalid)
makeFile(gif)
makeFile(other)

for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    file = file.lower()  # 文件名改为小写
    # 是文件
    if os.path.isfile(file_path):
        # 是图片类型：jpg、jpeg、png
        if file.endswith(".jpg") or file.endswith(".jpeg"):

            try:
                exif_dict = piexif.load(file_path)
                # 有 exif 信息
                if piexif.ExifIFD.DateTimeOriginal in exif_dict['Exif'].keys() and piexif.ExifIFD.DateTimeDigitized in exif_dict['Exif'].keys():
                    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal].replace(b"/", b":")
                    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized].replace(b"/", b":")

                    print(file_path, "有 exif 信息：", exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal], exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized])

                    # 填入替换后的信息
                    exif_bytes = piexif.dump(exif_dict)
                    piexif.insert(exif_bytes, file_path)

                else:
                    # 没有 exif 信息
                    print(file_path, "没有 exif 信息")
                    # 根据名称，创建exif信息，格式：b'2013:03:08 14:19:32'

                    # 方式1：截取前17位
                    date_string1 = file[0:17]
                    date = datetime.strptime(date_string1, '%Y-%m-%d %H%M%S')
                    DateTime = date.__format__('%Y:%m:%d %H:%M:%S')
                    # # 方式2：根据特定字符解析
                    # DateTime = ":".join(file.split()[0].split("-")) + " 12:00:00"

                    print(file_path, DateTime)
                    DateTime = DateTime.encode()
                    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = DateTime
                    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = DateTime

                    # 填入生成的信息
                    exif_bytes = piexif.dump(exif_dict)
                    piexif.insert(exif_bytes, file_path)
                    # 移动？
                    # shutil.move(file_path, invalid)

            except Exception as e:  # 未知错误
                print(file_path, e)
                shutil.move(file_path, invalid)

        # 其他格式：gif
        elif file.endswith(".gif"):
            shutil.move(file_path, gif)
            print(os.path.join(directory, file), "file is GIF!")

        # 其他格式：png（png没有exif信息）
        elif file.endswith(".png"):
            shutil.move(file_path, png)
            print(os.path.join(directory, file), "file is PNG!")

        # 其他格式：.DS_Store
        elif file.endswith(".ds_store"):
            print(os.path.join(directory, file), "file is DS_Store!")

        # 其他格式：
        else:
            shutil.move(file_path, other)
            print(os.path.join(directory, file), "unknown type of file！")
    else:
        print(os.path.join(directory, file), "不是文件")
