# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# import piexif
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#     file_path = "2017-05-31 162632(1).jpg"
#     # file_path = "IMG_1668.JPG"
#     # file_path = "IMG_1670.JPG"
#     exif_dict = piexif.load(file_path)
#
#     DateTimeOriginal = exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal]
#     DateTimeDigitized = exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized]
#
#     print(DateTimeOriginal, DateTimeDigitized)  # 从此处读取的信息来看，比较正常，不知道微信传输和保存到手机这两步，是否有影响
#     # print(exif_dict)
#     print(exif_dict['Exif'])  # 读取所有的exif信息


import piexif
import os
import shutil

# Loop over directory
directory = "Downloads/photo/"
invalid = "Downloads/photo/invalid/"

for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    if file.endswith(".jpg") or file.endswith(".JPG"):
        # modify DateTimeOriginal / DateTimeDigitized
        try:
            exif_dict = piexif.load(file_path)
            # key exist
            if piexif.ExifIFD.DateTimeOriginal in exif_dict['Exif'].keys() and piexif.ExifIFD.DateTimeDigitized in exif_dict['Exif'].keys():
                exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal].replace(b"/", b":")
                exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized].replace(b"/", b":")

                # dump it!
                exif_bytes = piexif.dump(exif_dict)
                piexif.insert(exif_bytes, file_path)

            else:
                print(file_path, "Key does not exist")
                # create timestamp from file name
                # b'2013:03:08 14:19:32'
                DateTime = ":".join(file.split()[0].split("-")) + " 12:00:00"
                DateTime = DateTime.encode()
                exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = DateTime
                exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = DateTime

                # dump it!
                exif_bytes = piexif.dump(exif_dict)
                piexif.insert(exif_bytes, file_path)
                # shutil.move(file_path, invalid)

        except Exception as e:  # 未知错误
            print(file_path, e)
            shutil.move(file_path, invalid)

    elif file.endswith(".png"):
        shutil.move(file_path, invalid)
        print(os.path.join(directory, file), "file is PNG!")

    else:
        print(os.path.join(directory, file), "Different type of file")
