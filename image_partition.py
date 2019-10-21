from PIL import Image
import os
from Prediction import *
import tkinter as tk
def call1(name):
    lol='Demo/images/'
    lol=lol+name
    #print(lol)
    dump(lol)
    
def crop(infile,height,width):
    im = Image.open(infile)
    imgwidth, imgheight = im.size
    print(height)
    for i in range(imgheight//height):
        for j in range(imgwidth//width):
            box = (j*width, i*height, (j+1)*width, (i+1)*height)
            yield im.crop(box)

def dump(infile):
    #infile="sajid.jpg"
    open('output/output1.txt', 'w').close()
    open('output/output2.txt', 'w').close()
    open('output/output3.txt', 'w').close()
    im = Image.open(infile)
    imgwidth, imgheight = im.size
    print(imgwidth)
    print(imgheight)
    height=350
    width=imgwidth
    start_num=1
    k=0
    for k,piece in enumerate(crop(infile,height,width),start_num):
        img=Image.new('RGB', (width,height), 255)
        img.paste(piece)
        path=os.path.join('temporary',"IMG-%s.png" % k)
        img.save(path)
        how(path)

       
        