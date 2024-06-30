import os
from PIL import Image

# todo 定义原始图片和处理后图片的目录
input_dir = "~/Downloader/阿里云盘/2024"
output_dir = "~/Downloader/阿里云盘/png"

# 创建处理后图片的目录（如果不存在）
os.makedirs(output_dir, exist_ok=True)


# 裁剪和压缩图片函数
def process_images():
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg"):
            input_filepath = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + ".png"
            output_filepath = os.path.join(output_dir, output_filename)

            try:
                with Image.open(input_filepath) as img:
                    # 剪裁图片
                    left = 60
                    top = 100
                    right = img.width - 60
                    bottom = img.height - 312
                    cropped_img = img.crop((left, top, right, bottom))

                    # 压缩图片
                    target_width, target_height = 758, 1024
                    resized_img = cropped_img.resize((target_width, target_height), Image.LANCZOS)

                    # 保存为 PNG
                    resized_img.save(output_filepath, "PNG")
                    print(f"Processed image saved as {output_filepath}")
            except Exception as e:
                print(f"Failed to process image {input_filepath}: {e}")


if __name__ == "__main__":
    process_images()
    print("All images have been processed.")
