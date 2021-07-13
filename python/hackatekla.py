#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
from os import system
import re
import json

folder = '/tmp/'
input_img   =    folder+'takatekla.png'
output_img  =    folder+'/takatekla_crop.png'
output_txt  =    folder+'/takatekla.txt'
output_json =    folder+'/takatekla.json'
hitzak = []

command = "/usr/bin/gocr "+output_img+" > "+output_txt

# irudia ebaki

left = 15
top = 166
right = 1295
bottom = 816

while True:
    try:
        img = Image.open(input_img)
        crop = img.crop((left, top, right, bottom)) 
        crop.save(output_img)
        break
    except:
        pass

# irudia testura pasatu

system(command)

# testua irakurri
testua = open(output_txt, "r").read()
# hutsuneak eta _ daukatenak kendu
hitzak = re.findall(r"([^\s_]+)", testua, re.MULTILINE)

# hitzak json bihurtu
with open(output_json, 'w') as f:
    json.dump(hitzak, f)