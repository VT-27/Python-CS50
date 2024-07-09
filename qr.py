import qrcode

img = qrcode.make("https://www.linkedin.com/in/vivekbtiwari/")
img.save("vivek.png", "PNG")