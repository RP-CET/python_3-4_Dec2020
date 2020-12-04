import os
from PIL import Image, ImageFilter, ImageOps

def watermark(im, mark, position):
    layer = Image.new("RGBA", im.size, (0,0,0,0))
    layer.paste(mark, position)
    return Image.composite(layer, im, layer)

files = os.listdir('img')

for file in files:
    if file.lower().endswith(".jpg"):
        
        im = Image.open("img/" + file)
        #im.thumbnail((60, 90), Image.ANTIALIAS)
        mark = Image.open("img/watermark.png")
        mark = mark.resize((100,100))
        mark.putalpha(128)
        
        width, height = im.size
        wm_w, wm_h = mark.size
        x = int(width/2 - wm_w/2)
        y = int(height/2 - wm_h/2)
        
        out = watermark(im, mark, (x,y))        
        out.save("watermark/" + file, "JPEG")
