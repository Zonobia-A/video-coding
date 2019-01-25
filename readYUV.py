import scipy.misc
import numpy as np
import cv2
import os


def yuv2bgr(filename, height, width, startfrm, total_420_frame):
    fp = open(filename, 'rb')
    framesize_420 = height * width * 3 // 2
    framesize = height * width
    h_h = height // 2
    h_w = width // 2
    fp.seek(0, 2)  # 设置文件指针到文件流的尾部
    ps = fp.tell()  # 当前文件指针位置
    numfrm = total_420_frame + (ps - total_420_frame * framesize_420) // framesize
    # numfrm = ps // framesize  # 计算输出帧数
    # print(numfrm)
    fp.seek(framesize * startfrm, 0)
    if not os.path.exists("news_400"):
        os.makedirs("news_400")
    for i in range(numfrm - startfrm):
        if i % 5 != 0:
            bgr_img = np.zeros ( shape=(height, width), dtype='uint8', order='C' )
            # bgr_img = np.zeros(shape=(height, width), dtype='uint8', order='C')
            # Ut = np.zeros(shape=(h_h, h_w), dtype='uint8', order='C')
            # Vt = np.zeros(shape=(h_h, h_w), dtype='uint8', order='C')

            for m in range(height):
                for n in range(width):
                    bgr_img[m, n] = ord(fp.read(1))
            # for m in range(h_h):
            #     for n in range(h_w):
            #         Ut[m, n] = ord(fp.read(1))
            # for m in range(h_h):
            #     for n in range(h_w):
            #         Vt[m, n] = ord(fp.read(1))
        else:
            Yt = np.zeros(shape=(height, width), dtype='uint8', order='C')
            Ut = np.zeros(shape=(h_h, h_w), dtype='uint8', order='C')
            Vt = np.zeros(shape=(h_h, h_w), dtype='uint8', order='C')
            YY = np.zeros_like(Yt, dtype='uint8')
            UU = np.zeros_like(Yt, dtype='uint8')
            VV = np.zeros_like(Yt, dtype='uint8')
            YUV = np.zeros(shape=(height, width, 3), dtype='uint8')
            for m in range(height):
                for n in range(width):
                    Yt[m, n] = ord(fp.read(1))
            for m in range(h_h):
                for n in range(h_w):
                    Ut[m, n] = ord(fp.read(1))
            for m in range(h_h):
                for n in range(h_w):
                    Vt[m, n] = ord(fp.read(1))
            UU[0: height - 1: 2, 0: width - 1: 2] = Ut[:, :]
            UU[0: height - 1: 2, 1: width: 2] = Ut[:, :]
            UU[1: height: 2, 0: width - 1: 2] = Ut[:, :]
            UU[1: height: 2, 1: width: 2] = Ut[:, :]
            VV[0: height - 1: 2, 0: width - 1: 2] = Vt[:, :]
            VV[0: height - 1: 2, 1: width: 2] = Vt[:, :]
            VV[1: height: 2, 0: width - 1: 2] = Vt[:, :]
            VV[1: height: 2, 1: width: 2] = Vt[:, :]
            YUV[:, :, 0] = Yt
            YUV[:, :, 1] = UU
            YUV[:, :, 2] = VV
            bgr_img = cv2.cvtColor(YUV, cv2.COLOR_YCrCb2BGR)
        print("Extract frame %d " % (i + 1))

        scipy.misc.imsave('news_400/'+str(i)+'.png', bgr_img)

    fp.close()
    return None

if __name__ == '__main__':
    _ = yuv2bgr(filename='C:/Users/Administrator/Desktop/HM-16.0/bin/rec.yuv', height=288, width=352, startfrm=0, total_420_frame=60)