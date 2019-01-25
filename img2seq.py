import cv2
import scipy.misc
import os
import numpy as np
import glob
import matplotlib.pyplot as pl

input_dir = "color_pics"
output_dir = "video"
ROW = 640
COL = 720
FRAME = 600
is_gray = False


def get_name(path):
    name, _ = os.path.splitext(os.path.basename(path))
    return name


def img2seq(input_dir, height, width, frame, output_dir, is_gray):
    # print(os.path.exists(output_dir))
    if not os.path.exists(input_dir) or not os.path.exists(output_dir):
        print("Invalid input_dir or output_dir")
    else:
        with open(output_dir+"/target.yuv", "wb") as of:
            input_paths = glob.glob(os.path.join(input_dir, '*.png'))
            input_paths = sorted(input_paths, key=lambda path: int(get_name(path)))
            dic_y = np.zeros(shape=[height, width, frame])
            if not is_gray:
                dic_uu = np.zeros(shape=[height, width, frame])
                dic_vv = np.zeros(shape=[height, width, frame])
                dic_u = np.zeros(shape=[height//2, width//2, frame])
                dic_v = np.zeros(shape=[height//2, width//2, frame])
            for i in range(10):
                img = scipy.misc.imread(input_paths[i])
                if not is_gray:
                    img2yuv = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
                    dic_y[:, :, i] = img2yuv[:, :, 0]
                    pic_Y = dic_y[:, :, i]
                    dic_uu[:, :, i] = img2yuv[:, :, 1]
                    dic_vv[:, :, i] = img2yuv[:, :, 2]
                    dic_u[:, :, i] = dic_uu[0: height - 1: 2, 0: width - 1: 2, i]
                    dic_v[:, :, i] = dic_vv[0: height - 1: 2, 0: width - 1: 2, i]
                    pic_U = dic_u[:, :, i]
                    pic_V = dic_v[:, :, i]
                    for j in range(height):
                        for k in range(width):
                            of.write(pic_Y[j, k].astype(np.int8))
                    for j in range(height//2):
                        for k in range(width//2):
                            of.write(pic_U[j, k].astype(np.int8))
                    for j in range(height//2):
                        for k in range(width//2):
                            of.write(pic_V[j, k].astype(np.int8))
                else:
                    pic_Y = img
                    for j in range(height):
                        for k in range(width):
                            of.write(pic_Y[j, k].astype(np.int8))


img2seq(input_dir, ROW, COL, FRAME, output_dir, is_gray)
