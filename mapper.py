import numpy as np
from openslide import open_slide
from openslide.deepzoom import DeepZoomGenerator
import os
import sys
  
# to remove leading and trailing whitespace
image_path = sys.argv[1]
# split the line into words
words = image_path.split("/")
svs_file = words[len(words)-1]#"23-168-001-004.svs"
slide = open_slide(f"{image_path}")
current_svs_file_nm = svs_file.split(".")[0]
print(current_svs_file_nm)
tiles = DeepZoomGenerator(slide, tile_size=1024, overlap=0, limit_bounds=False)
level = tiles.level_count - 1
cols, rows = tiles.level_tiles[level]
#os.system(f'mkdir processing/tiles/{current_svs_file_nm}_{level}')
# we are looping over the words array and printing the word
# with the count of 1 to the STDOUT
for col in range(cols):
    for row in range(rows):
    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # Reduce step, i.e. the input for reducer.py
        img = tiles.get_tile(level, (0, 0))
        img_d = list(img.getdata())
        #dt=np.dtype
        np_img = np.asarray(img)
        data = np_img.tobytes()
        print(f"{level}_{str(col)}_{str(row)}_{current_svs_file_nm}\t{data}")