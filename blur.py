from PIL import Image, ImageFilter
import sys
print(sys.executable)

before = Image.open("Front.bmp")
 
after = before.filter(ImageFilter.BoxBlur(10))

after.save("outblur.bmp")
                      