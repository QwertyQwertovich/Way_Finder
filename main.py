# Made by Kharitonov Alexander
# MIT License
#Copyright 2021 Kharitonov Alexander

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import random
from PIL import Image, ImageDraw
import colorsys
image = Image.open("image.png")
width = image.size[0]
height = image.size[1]
pix = image.load()
x = width - 2
y = height - 2
ex = 10
ey = 10
rot = 270
draw = ImageDraw.Draw(image)
for i in range(width):
    for j in range(height):
        a = pix[i, j][0]
        b = pix[i, j][1]
        c = pix[i, j][2]
        draw.point((i, j), (a, b, c))
i = 0
while x > ex or y > ey:
    i = i + 1
    if i > 360:
        i = 0
    c = colorsys.hsv_to_rgb(i / 360, 1, 1)
    r, g, b = round(c[0] * 255), round(c[1] * 255), round(c[2] * 255)
    draw.point((x, y),(r,g,b))
    if rot == 0:
        if pix[x + 1, y][0] > 200:
            rot = 90
        else:
            if pix[x, y - 1][0] < 200:
                rot = 90
                y = y - 1
            else:
                x = x + 1
    elif rot == 90:
        if pix[x, y - 1][0] > 200:
            rot = 180
        else:
            if pix[x - 1, y][0] < 200:
                rot = 180
                x = x -1
            else:
                y = y - 1
    elif rot == 180:
        if pix[x - 1, y][0] > 200:
            rot = 270
        else:
            if pix[x, y + 1][0] < 200:
                rot = 270
                y = y + 1
            else:
                x = x - 1
    elif rot == 270:
        if pix[x, y + 1][0] > 200:
            rot = 0
        else:
            if pix[x + 1, y][0] < 200:
                rot = 0
                x = x + 1
            else:
                y = y + 1
    #print(rot, x, y)
print(x, y)
image.save("ans.png", "PNG")
del draw