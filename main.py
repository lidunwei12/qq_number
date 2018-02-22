# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:21:28 2017

@author: boblee
"""
from PIL import Image
from src.serach import dhash
from src.serach import hash_image_save
from src.qq import qq_image
import os
DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), 'image'))
if not os.path.isdir(DATA_HOME):
    os.mkdir(DATA_HOME)


def main(qq_number, numebr_start, number_end):
    count = qq_image(numebr_start, number_end)
    hash_image_save()
    file_jpg = str(qq_number)+'.jpg'
    image = Image.open(DATA_HOME+'/'+file_jpg)
    image_hash = dhash(image)
    result = []
    file = open(os.path.join(os.path.dirname(__file__)) +"/hash.txt")
    for line in file:
     if line.find(image_hash) != -1:
         result.append(line[0:line.find('.jpg')])
    return result
print(main(1294163174, 1294163140, 1294163300))
