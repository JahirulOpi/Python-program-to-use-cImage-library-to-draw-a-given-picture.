from cImage import *

p1 = Pixel(0,0,255)
p2 = Pixel(255,0,0)
im = EmptyImage(300,300)
x = 299
w = ImageWin("My Image", 300, 300)
for i in range (300):
    im.setPixel(i, i, p1)
for i in range (300):
    im.setPixel(x, i, p1)
    x = x - 1
for i in range (150):
    im.setPixel(150, i+150, p2)

im.draw(w)
