import os
from lunar_python import Lunar
from PIL import Image, ImageDraw, ImageFont

# 定义保存图片的目录
output_dir = "/Users/george/Downloads/Downloader/阿里云盘/generate"
os.makedirs(output_dir, exist_ok=True)

# 设置字体（确保路径正确或使用系统字体）
font_path = "/Users/george/Library/Fonts/思源宋体（Super OTC）SourceHanSerif.ttc"  # 你可以换成你自己的字体路径
font_size_3xl = 300
font_size_large = 48
font_size_medium = 36
font_size_small = 24

font_large = ImageFont.truetype(font_path, font_size_large)
font_medium = ImageFont.truetype(font_path, font_size_medium)
font_small = ImageFont.truetype(font_path, font_size_small)


# 生成每日的日历图片
def generate_yearly_calendar_images():
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                generate_single_day_calendar_image(month, day)
            except ValueError:
                # 忽略无效的日期（例如：2月30日）
                continue


# 生成单日的日历图片
def generate_single_day_calendar_image(month, day):
    try:
        # 获取农历和公历信息
        lunar = Lunar.fromYmd(2024, month, day)
        solar = lunar.getSolar()

        # 创建灰度图片
        image = Image.new("L", (758, 1024), "white")
        draw = ImageDraw.Draw(image)

        # 添加背景色块
        draw.rectangle([(0, 0), (758, 1024)], fill="#F8F8F8")

        # 添加边框
        border_width = 5
        draw.rectangle(
            [(border_width, border_width), (758 - border_width - 1, 1024 - border_width - 1)],
            outline="black", width=border_width
        )

        # 绘制公历信息
        solar_text = f"{solar.getYear()}年{solar.getMonth()}月{solar.getDay()}日"
        draw.text((50, 50), solar_text, fill="black", font=font_large)

        # 绘制农历信息
        lunar_text = f"农历: {lunar.getYearInChinese()}年{lunar.getMonthInChinese()}月{lunar.getDayInChinese()}日"
        draw.text((50, 150), lunar_text, fill="black", font=font_medium)

        # 添加节气信息
        jieqi = lunar.getJieQi()
        if jieqi:
            jieqi_text = f"节气: {jieqi}"
            draw.text((50, 250), jieqi_text, fill="black", font=font_medium)

        # 添加其他农历信息
        lunar_detail_text = f"{lunar.getDayInGanZhi()}日, {lunar.getYearShengXiao()}年"
        draw.text((50, 350), lunar_detail_text, fill="black", font=font_small)

        # 添加日期框
        date_box_width, date_box_height = 200, 100
        date_box_top = 450
        draw.rectangle(
            [(279, date_box_top), (279 + date_box_width, date_box_top + date_box_height)],
            outline="black", width=2
        )

        # 绘制日期框内的日期
        draw.text((320, 475), f"{solar.getDay()}", fill="black", font=font_size_3xl)

        # 添加装饰性元素
        draw.line([(50, 500), (708, 500)], fill="black", width=1)

        # 保存图片
        output_filename = os.path.join(output_dir, f"2024_{month:02d}_{day:02d}.png")
        image.save(output_filename, "PNG")
        print(f"Generated image for {solar_text}")

    except ValueError:
        # 忽略无效的日期（例如：2月30日）
        print(f"无效的日期 {month:02d}/{day:02d}")


if __name__ == "__main__":
    # 生成整年的每日日历图片
    # generate_yearly_calendar_images()

    # 示例：生成特定日期的日历图片
    generate_single_day_calendar_image(7, 1)

    print("All images have been generated.")
