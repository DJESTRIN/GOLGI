
import os
#import pandas as pd
#from glob import glob
from openslide import open_slide
#from pprint import pprint
import matplotlib.pyplot as plt
#from PIL import Image
import numpy as np
from skimage.color import rgb2gray
import ipdb

#user inputs a file
file = input("Enter file name: ")    # TO BE CHANGED
#opens the file
slide = open_slide(file)

from openslide.deepzoom import DeepZoomGenerator

tiles = DeepZoomGenerator(slide, tile_size=500, overlap=0, limit_bounds=False)
#level = tiles.level_count

#combining levels into one
ipdb.set_trace()
#tiles = np.array(tiles)              # NOT SURE IF WORKS
#tiles = np.max(tiles, axis=level)

#level = tiles.level_count - 1
cols, rows = tiles.level_tiles[1]

os.path.split(file)
parent_dir, filename=os.path.split(file)
new_dir = parent_dir + "/" + "tiled_images"
tile_dir = os.mkdir(new_dir)

for row in range(rows):
    for col in range(cols):
        tile_name = os.path.join(tile_dir,'/' (col, row))
        temp_tile = tiles.get_tile(level, (col, row))
        temp_tile_RGB = temp_tile.convert('RGB')
        temp_tile_np = np.array(temp_tile_RGB)
        inverted_tile = 255 - rgb2gray(temp_tile_np)
        np.save(tile_name.npy, inverted_tile)
        
        




        





            


