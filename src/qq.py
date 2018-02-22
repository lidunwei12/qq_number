# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:21:28 2017

@author: boblee
"""
import urllib.request
import os
DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'image'))
if not os.path.isdir(DATA_HOME):
    os.mkdir(DATA_HOME)


def url_image(url, file_home):
    try:
        data = urllib.request.urlopen(url).read()
        f = open(file_home, 'wb')
        f.write(data)
    except Exception as e:
        data = ''
    return data


def qq_image(numebr_start, number_end):
    count = 0
    try:
        for i in range(numebr_start, number_end):
            url = 'http://q1.qlogo.cn/g?b=qq&nk='+str(i)+'&s=100'
            url_image(url, DATA_HOME + '/' + str(i)+'.jpg')
    except Exception as e:
        print(e)
    return count

# qq_image(1294163140, 1294163200)
