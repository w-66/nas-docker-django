from random import randint,choices
from PIL import Image, ImageDraw, ImageFont
import string

# 生成数字或字母的验证码
def generate_auth_code_image(size=(120, 30),
                        position_offset_y=0,
                        bg_color=(255, 255, 255),
                        font_size=30,
                        font_type='/www/django_www/static/font/Adec.ttf',
                        length=4,
                        draw_lines=True,
                        line_num=(1, 2),
                        draw_points=True,
                        point_chance=2):
    """
    生成图片验证码
    :param size: 图片大小，默认为(120, 30)
    :param position_offset_y: 字符串y轴位置偏移量
    :param bg_color: 背景颜色，默认为白色
    :param font_size: 字体大小，默认为20
    :param font_type: 字体类型，默认为arial.ttf
    :param length: 验证码长度，默认为4
    :param draw_lines: 是否画干扰线，默认为True
    :param line_num: 干扰线的数量范围，默认为(1, 2)
    :param draw_points: 是否画干扰点，默认为True
    :param point_chance: 干扰点出现的概率，范围为0到100，默认为2
    :return: (image, code)
    """
    width, height = size
    # 创建一个Image对象并设置背景颜色
    image = Image.new('RGB', size, bg_color)
    # 创建Font对象
    font = ImageFont.truetype(font_type, font_size)
    # 创建Draw对象
    draw = ImageDraw.Draw(image)

    # 生成随机数字字母验证码字符串
    all_chars = string.digits + string.ascii_letters
    code = ''.join(choices(all_chars, k=length))
    ## 生成数字0-9
    ## code = ''.join([str(randint(0, 9)) for _ in range(length)])
    ## 生成字母验证码 
    ## code = ''.join([str(random.choice(string.ascii_letters)) for _ in range(length)])
    
    # 绘制验证码字符串
    for i in range(length):
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        x = width / length * i + randint(-5, 5)
        y = randint(-5, 5)
        draw.text((x, y+position_offset_y), code[i], font=font, fill=color)

    # 绘制干扰线
    if draw_lines:
        for _ in range(randint(*line_num)):
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
            begin = (randint(0, width), randint(0, height))
            end = (randint(0, width), randint(0, height))
            draw.line([begin, end], fill=color)

    # 绘制干扰点
    if draw_points:
        for w in range(width):
            for h in range(height):
                tmp = randint(0, 100)
                if tmp > 100 - point_chance:
                    color = (randint(0, 255), randint(0, 255), randint(0, 255))
                    draw.point((w, h), fill=color)

    return code, image


if __name__ == "__main__":
    code, image= generate_auth_code_image(draw_points=True, point_chance=1, line_num=(1, 3))
    
    print(code)
    image.show(image)
