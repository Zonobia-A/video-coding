import scipy.misc
import numpy as np
import cv2
import os


def yuv2bgr(filename, height, width, startfrm):
    fp = open(filename, 'rb')
    framesize = height * width
    fp.seek(0, 2)
    ps = fp.tell()
    numfrm = ps // framesize
    fp.seek(framesize * startfrm, 0)
    if not os.path.exists("data/silent/silent-400-QP42"):
        os.makedirs("data/silent/silent-400-QP42")
    for i in range(numfrm - startfrm):
        bgr_img = np.zeros ( shape=(height, width), dtype='uint8', order='C' )
        for m in range(height):
            for n in range(width):
                bgr_img[m, n] = ord(fp.read(1))
        print("Extract frame %d " % (i + 1))
        scipy.misc.imsave('data/silent/silent-400-QP42/'+str(i)+'.png', bgr_img)
    fp.close()
    return None


if __name__ == '__main__':
    _ = yuv2bgr(filename='C:/Users/Administrator/Desktop/HM-16.0/bin/rec.yuv', height=288, width=352, startfrm=0)