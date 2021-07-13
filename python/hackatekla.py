#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
from os import system
import re
import json

config = json.loads(open("config.json", "r").read())

input_img   =    config['folder']+config['input_img']
output_img  =    config['folder']+config['output_img']
output_txt  =    config['folder']+config['output_txt']
output_json =    config['folder']+config['output_json']

hitzak = []

# OCR shell komandoa
command = "/usr/bin/gocr "+output_img+" > "+output_txt

# irudia ebaki
while True:
    try:
        img = Image.open(input_img)
        crop = img.crop((config['left'], config['top'], config['right'], config['bottom'])) 
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
# gutxienez 2 letra izan behar ditu
hitzak = list(filter(lambda i: len(i)>1 , hitzak))

# hitzak json bihurtu
with open(output_json, 'w') as f:
    json.dump(hitzak, f)