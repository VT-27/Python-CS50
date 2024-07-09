from PIL import Image, ImageFilter

before = Image.open("Front.bmp")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("outpu1.bmp")