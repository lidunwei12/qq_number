# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:21:28 2017

@author: boblee
"""
from PIL import Image
import os
DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'image'))
if not os.path.isdir(DATA_HOME):
    os.mkdir(DATA_HOME)


def dhash(image, hash_size=8):
    image = image.convert('L').resize((hash_size + 1, hash_size), Image.ANTIALIAS,)
    difference = []
    for row in range(hash_size):
        for col in range(hash_size):
            pixel_left = image.getpixel((col, row))
            pixel_right = image.getpixel((col + 1, row))
            difference.append(pixel_left > pixel_right)
    decimal_value = 0
    hex_string = []
    for index, value in enumerate(difference):
        if value:
            decimal_value += 2 ** (index % 8)
        if (index % 8) == 7:
            hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
            decimal_value = 0

    return ''.join(hex_string)


def hash_write(content):
    with open("hash.txt", "a", encoding='utf-8') as f:
        f.write(content)
        f.write('\n')
    return True


def hash_image_save():
    for file_jpg in os.listdir(DATA_HOME):
        try:
            orig = Image.open(DATA_HOME+'/'+file_jpg)
            content = file_jpg+'  '+str(dhash(orig))
            hash_write(content)
        except Exception as e:
            print(e)
    return True