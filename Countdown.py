from PIL import Image, ImageDraw


def countdown(value):
    value = str(value)
    mode = "RGB"
    img = Image.new(mode, (300, 450), color=0)
    draw = ImageDraw.Draw(img)
    draw.text((50, 50), value, fill="red", font=None, align="Right")
    img.save("countdown.png")


countdown(1)
