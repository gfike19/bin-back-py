from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def writeLines(draw, msg, img_size, txt_color, font, text_size):
    leng = len(msg)
    idx = 0
    for x in range(1, img_size[0] - 1, text_size):
        for y in range(1, img_size[1] - 1, text_size):
            draw.text((y,x),msg[idx % leng], txt_color, font=font)
            idx += 1

try:
    img = Image.new("RGB", (400,400), "black")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 16)

    writeLines(draw, "testing testing 1 2 3 ", (400,400), "white", font)
    img.save("test.jpg")
except Exception as e:
    print("Error occured: " + str(e))

print("Image has been created!")
