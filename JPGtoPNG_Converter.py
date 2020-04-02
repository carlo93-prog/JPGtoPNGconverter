# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:10:00 2020

@author: carlo
"""


import os
from PIL import Image


def JPGtoPNG_Converter(name_new_folder):
    pic_folder= os.getcwd()
    new_folder=os.path.join(pic_folder,name_new_folder)
    
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
        print(f'{name_new_folder} does not exist. I will create it')
    else:
        print('this folder already exists')
    
    n_img=1
    
    for filename in os.listdir(pic_folder):
        if filename.endswith(".jpg"):
            im = Image.open(filename)
            name='img'+str(n_img)
            n_img+=1
            fullpath = os.path.join(new_folder, name)
            im.save(f'{fullpath}.png','png')
            print(f"we are adding new images in your {name_new_folder} folder")
            continue
        else:
            continue



    