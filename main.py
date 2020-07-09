from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def getBinMsg(msg, spaces):
    lst = []
    for char in msg:
        lst.append(ord(char))

    msg = ""
    for each in lst:
        msg += "{0:b}".format(each)

    return msg 

def writeLinesRTL(draw, msg, img_size, txt_color, font, text_size):
    leng = len(msg)
    idx = 0
    for x in range(0, img_size[1], text_size + text_size // 2):
        for y in range(0, img_size[0], text_size):
            draw.text((y,x),msg[idx], txt_color, font=font)
            idx += 1
            if idx > leng - 1:
                idx = 0

def writeLinesTTB(draw, msg, img_size, txt_color, font, text_size):
    leng = len(msg)
    idx = 0
    for x in range(0, img_size[0], text_size):
        for y in range(0, img_size[1], text_size + text_size // 2):
            draw.text((x,y),msg[idx], txt_color, font=font)
            idx += 1
            if idx > leng - 1:
                idx = 0

def main():   
    name = input("What will be the name of this image be?: ")
    wid = int(input("What is the width of this image?: "))
    ht = int(input("What is the height of this image?: "))
    img_size = (wid, ht)
    txt_color = input("What's the color of the text?: ")
    back = input("What is the background color for this immage?: ")
    msg = input("What is the message?: ")
    bin_stat = input("Binary? (y/n) ")
    if bin_stat == "y":
        spaces = ""
        addSpaces = input("Convert spaces to binary? (y/n) ")
        msg = getBinMsg(msg)
    text_size = int(input("What size will the font be?: "))
    direction = input("Draw the image right to left (RTL) or top to bottom (TTB)? ")
    e = ""
    # name = "test"
    # img_size = (1024, 768)
    # txt_color = "white"
    # back = "black"
    # msg = "test"
    # bin_stat = "n"
    # text_size = 24
    # direction = "RTL"
    try:
        img = Image.new("RGB", img_size, back)
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype("arial.ttf", text_size)
        # draw.text((x, y),"Sample Text",(r,g,b))
        if direction == "RTL":
            writeLinesRTL(draw, msg, img_size, txt_color, font, text_size)
        if direction == "TTB":
            writeLinesTTB(draw, msg, img_size, txt_color, font, text_size)
        name += ".jpg"
        img.save(name)
        print(name, "image was sucessfully made!")
    except Exception as e:
        print("\n" + "Error occured: " + str(e))

if __name__ == "__main__":
    main()