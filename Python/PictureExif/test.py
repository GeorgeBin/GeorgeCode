import piexif
from datetime import datetime


def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    # file_path = "2017-05-31 162632(1).jpg"
    # # file_path = "IMG_1668.JPG"
    # # file_path = "IMG_1670.JPG"
    # exif_dict = piexif.load(file_path)
    #
    # DateTimeOriginal = exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal]
    # DateTimeDigitized = exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized]
    #
    # print(DateTimeOriginal, DateTimeDigitized)  # 从此处读取的信息来看，比较正常，不知道微信传输和保存到手机这两步，是否有影响
    # # print(exif_dict)
    # # print(exif_dict['Exif'])  # 读取所有的exif信息

    date_string = "2017-05-31 162632(1).jpg"
    # date_string = "2017-05-31 162632.jpg"
    # date_string = "2017-05-31 162632"

    # DateTime = ":".join(date_string.split()[0].split("-")) + " 12:00:00"
    # print(DateTime)
    # DateTime = DateTime.encode()
    # print(DateTime)

    # # 按指定字符截取
    # date_string2 = date_string.split(".")[0]
    # print(date_string2)
    #
    # date_string3 = date_string2.split("(")[0]
    # print(date_string3)
    #
    # date_object = datetime.strptime(date_string3, '%Y-%m-%d %H%M%S')
    # print(date_object)

    # 截取前17位
    date_string55 = date_string[0:17]
    print(date_string55)
    date_string555 = datetime.strptime(date_string55, '%Y-%m-%d %H%M%S')
    date_string555 = date_string555.__format__('%Y:%m:%d %H:%M:%S')
    print(date_string555)

    # date_string = "2017-05-31 162632"
    # date_string5555 = date_string555.replace("-", ":", 2)
    # print(date_string5555)
