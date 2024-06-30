import os
import requests

# todo 此方式不可行，只能下载到距离当前日期约一个月的图片

# 定义基本的 URL 格式
base_url = "https://img.owspace.com/Public/uploads/Download/2024/{:02d}{:02d}.jpg"

# todo 定义保存图片的目录
save_dir = "~Download/owspace/2024/"

# 创建保存图片的目录（如果不存在）
os.makedirs(save_dir, exist_ok=True)

# 循环下载每个月的每一天的图片
for month in range(1, 13):
    for day in range(1, 32):
        # 构建图片的 URL
        image_url = base_url.format(month, day)

        # 定义保存图片的文件名
        image_filename = os.path.join(save_dir, f"2024_{month:02d}_{day:02d}.jpg")

        try:
            # 请求下载图片
            response = requests.get(image_url)

            # 如果请求成功（状态码为200）
            if response.status_code == 200:
                # 保存图片到本地文件
                with open(image_filename, 'wb') as file:
                    file.write(response.content)
                print(f"Downloaded: {image_filename}")
            else:
                print(f"Failed to download: {image_url} (Status code: {response.status_code})")

        except requests.RequestException as e:
            print(f"Error downloading {image_url}: {e}")

print("Download complete.")
