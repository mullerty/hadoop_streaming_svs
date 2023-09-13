import sys

import numpy as np
from PIL import Image

for line in sys.stdin:
    path = sys.argv[1]
    parts = line.split("\t")
    sub_p = parts[0].split("_")
    level = int(sub_p[0])
    col = int(sub_p[1])
    row = int(sub_p[2])
    name = sub_p[3]
    shape = np.frombuffer(parts[1], dtype=np.uint8)
    print(shape)
    shape = shape.reshape((1024, 1024, 3))
    tile_img = Image.fromarray(shape)
    tile_img.save(f'{path}/{name}_{level}/{col}_{row}.jpeg', format='jpeg', quality=90)