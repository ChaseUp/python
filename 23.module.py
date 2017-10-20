# 模块

from PIL import Image
im = Image.open('./img/test.png')
print(im.format, im.size, im.mode)
