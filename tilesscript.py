
"""this script takes the path to the directory with all the files and then tiles all the .mrvs images in the directory
then it saves the tiled images into new folders organized by levels also inverts the images """

#Import dependencies
from openslide import open_slide
import openslide
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import os
import glob
from openslide.deepzoom import DeepZoomGenerator
import tqdm
import argparse
import ipdb

# primary function for conversion
def main(path):
    #list of files that need to be tiled
    files = glob.glob(path + '*.mrxs')
    #create new directory to add all the tiled images
    directory = "tiled_images"
    new_path = os.path.join(path, directory)
    os.mkdir(new_path)

    #iterate through all the files
    for file in files:
        #opens the file
        slide = open_slide(file)
        #creates the tiles
        tiles = DeepZoomGenerator(slide, tile_size=500, overlap=0, limit_bounds=False)
        #finds how many levels in tiles
        levels = tiles.level_count
        #actual file name
        filename = file.split('.')
        filename_new = filename[0].split('/')
        name = len(filename_new) - 1
        filename_final = filename_new[name]
        newer_path = os.path.join(new_path, filename_final)
        os.mkdir(newer_path)
        #iterate through each level and saves tiles
        for l in tqdm.tqdm(range(levels)):
            cols, rows = tiles.level_tiles[l]
            new_path_folder = newer_path+'/level_'+str(l)
            os.mkdir(new_path_folder)
            for row in range(rows):
                for col in range(cols):
                    tile_name = os.path.join(new_path_folder,'%d_%d' % (col, row))
                    print("Now saving tile with title: ", tile_name)
                    temp_tile = tiles.get_tile(l, (col, row))
                    temp_tile_RGB = temp_tile.convert('RGB')
                    temp_tile_np = np.array(temp_tile_RGB)

                    # Convert to gray scale:
                    img_gray=np.mean(temp_tile_np,axis=2)
                    #R, G, B = temp_tile_np[:,:,0], temp_tile_np[:,:,1], temp_tile_np[:,:,2]   Does this work?
                    #img_gray = 0.2989 * R + 0.5870 * G + 0.1140 * B       Does this work?

                    #invert image
                    img_inverted = 255 - img_gray
                    plt.imsave(tile_name + ".tiff", img_inverted)   #will this down sample image?
 
if __name__=='__main__':
  # Command line interface
  try:
      parser = argparse.ArgumentParser(description="Convert mrxs files to tiled tiff images")
      parser.add_argument("--input", type=str, help="The directory containing the input mrxs files ",required=True)
      args = parser.parse_args()
      ipdb.set_trace()
      main(args.input)
  except:
      path=input("directory")
      main(path)
