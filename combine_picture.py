import os
import glob
import numpy as np
from PIL import Image
import scipy.misc

def get_name(path):
    name, _ = os.path.splitext(os.path.basename(path))
    return name


def combine_pictures(width, height, path, output_path, LCU_SIZE):

    col = width // LCU_SIZE
    raw = height // LCU_SIZE
    separate = col * raw
    input_paths = glob.glob(os.path.join(path, '*.jpg'))
    input_paths = sorted(input_paths, key=lambda path: int(get_name(path)))
    length = len(input_paths)
    total_pictures = length // separate
    print(total_pictures)
    for i in range(total_pictures):
        temp_pic = np.zeros(shape=(raw*LCU_SIZE, col*LCU_SIZE, 3))
        image_start = i * separate
        for j in range(separate):
            sub_image = Image.open(input_paths[i * separate + j])
            sub_image = np.array(sub_image)
            x_index = j // col
            y_index = j % col
            temp_pic[x_index*LCU_SIZE : (x_index+1)*LCU_SIZE, y_index*LCU_SIZE:(y_index+1)*LCU_SIZE, : ] = sub_image[:,:,:]
        scipy.misc.imsave(output_path+str(i+1)+'.png', temp_pic)


combine_pictures(768, 512, 'H:/420_all/', 'H:/real_image/', 128)