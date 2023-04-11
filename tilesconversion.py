# -*- coding: utf-8 -*-

import cv2
import os, glob
import argparse
import joblib
from tqdm import tqdm
from multiprocessing import Pool

#directory = args.name

#function to resize the image    
def tile_image(image):
    
    img = cv2.imread(image, 0) #image in grayscale

    width = img.shape[0]
    height = img.shape[1]
    
    if (len(img.shape) > 2):
        print("Warning. Will skip to next file")
        return
    
    img_width = 500
    img_height = 500
    
    os.path.split(image)
    parent_dir, filename=os.path.split(image)
    new_dir = parent_dir+"tiled_images"
    os.mkdir(new_dir)
    filename_real,_=filename.split('.')
    
    for x in range (0, width, img_width):
        for y in range (0, height, img_height):
            tile = img[y:y+img_width,x:x+img_height]
    
            #cv2.imwrite(image + str(x) + '_' + str(y)+".tiff", tile)
            #new_tile = cv2.imwrite(image + str(x) + '_' + str(y)+".tiff", tile)

            #saving files to directory
            FINAL_STRING = new_dir+"/"+filename_real+str(x)+'_'+str(y)+".tiff"
            cv2.imwrite(FINAL_STRING, tile)
    
    return 0

#main function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', type=str, required=True)
    parser.add_argument('--parallel', type=int, required=1)
    args = parser.parse_args()
    os.chdir(args.directory)
    files_list = glob.glob("*.tiff")
    if(args.parallel==True):
        with Pool() as p:
            p.map(tile_image, files_list)
    else:
        for image in tqdm(files_list):
            tile_image(image)
    
#running the main function
if __name__=="__main__":
    main()

