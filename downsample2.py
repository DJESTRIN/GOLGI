#!/usr/bin/env python3

''' this script downscales images '''

import os
import glob
import argparse
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

def main(path):
    if path[-1]!="/":
        path=path+"/"
    #list of files that need to be downscaled
    files = glob.glob(path + '*.mrxs')
    #create new directory to add all the downscaled images
    directory = "downsampled_images_pil"
    new_path = os.path.join(path, directory)
    if os.path.exists(new_path)==False:
        os.mkdir(new_path)
     
    #iterates through all the files
    for file in files:
        # opens file as image
        image = Image.open(file)
        # resizes image
        # 200 by 200 is for testing can be changed (same as for downsample1.py)
        new_image = image.resize((200,200))
        
        filename = file.split('.')
        filename_new = filename[0].split('/')
        name = len(filename_new) - 1
        filename_final = filename_new[name] + "_downscaled"

        # creating file name
        filename = file.split('.')
        filename_new = filename[0].split('/')
        name = len(filename_new) - 1
        filename_final = filename_new[name] + "_downscaled"
        
        # saving the file
        new_image.save(new_path + '/' + filename_final + ".tiff")
        
if __name__=='__main__':
    # command line interface
    parser = argparse.ArgumentParser(description="downscale .mrxs images to .tiff")
    parser.add_argument("input", type=str, help="the directory containing the input .mrxs files ")
    args = parser.parse_args()
    main(args.input)
        