from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import scipy.misc
import numpy as np
import os
import glob
from PIL import Image
IMAGE_SIZE = 128


def imcrop(Yt, height, width, image_size, frame):
    col = width // image_size
    raw = height // image_size
    sum = col * raw
    image_sub = np.zeros(shape=(col * raw, image_size, image_size), dtype='uint8')
    for i in range(raw):
        for j in range(col):
            # print('para: ', j*image_size, i*image_size)
            image_sub[i * col + j] = Yt[i*image_size: (i+1)*image_size, j*image_size: (j+1)*image_size]
            scipy.misc.imsave('../对比实验/mother-daughter_cif_256x256/400_all/' + str(frame*sum+i * col + j)+'.jpg', image_sub[i * col + j])


def get_name(path):
    name, _ = os.path.splitext(os.path.basename(path))
    return name


PATH = "../对比实验/mother-daughter_cif_256x256/400/"
input_paths = glob.glob(os.path.join(PATH, '*.png'))
input_paths = sorted(input_paths, key=lambda path: int(get_name(path)))
length = len(input_paths)
if not os.path.exists("../对比实验/mother-daughter_cif_256x256/400_all"):
    os.makedirs("../对比实验/mother-daughter_cif_256x256/400_all")
for i in range(length):
    # if i % 5 == 0:
    image = scipy.misc.imread(input_paths[i])
    imcrop(image, 256, 256, IMAGE_SIZE, i)
    print("finish cut pictures: " + str(i))