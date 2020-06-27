from PIL import Image, ImageDraw
def countdown():
    img = Image.new('1', (300, 450), color=0)
    draw = ImageDraw.Draw(img)
    draw.text((10,10), "Hello World", fill="red")
    img.save("countdown.png")

countdown()
