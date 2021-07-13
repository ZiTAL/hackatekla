#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
from sys import exit

left = 15
top = 166
right = 1295
bottom = 816

while True:
    try:
        img = Image.open(r"/tmp/takatekla.png")
        crop = img.crop((left, top, right, bottom)) 
        crop.save("/tmp/takatekla_crop.png")
        break
    except:
        pass
exit()
    