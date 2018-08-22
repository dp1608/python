# -*- coding: utf-8 -*-
# @StartTime : 2018/8/17 12:42
# @EndTime :
# @Author  : Andy
# @Site    : https://www.kaggle.com/inversion/run-length-decoding-quick-start/notebook
# @File    : pre_process.py
# @Software: PyCharm

"""
此代码为预处理图像
图像原格式为，游程编码格式，有船的位置有所谓的（mask）
根据图像标注转换为矩阵，对应地，有船的位置矩阵值为1（mask），没船的位置（background）为0
"""

import numpy as np
import pandas as pd
# from skimage.data import imread
import matplotlib.pyplot as plt
# from matplotlib.image import imread
from skimage.data import imread
from skimage import io
import time

class PreProcess(object):
    def __init__(self):

        self.shape = (768, 768)
        self.masks_name = '../input/train_ship_segmentations.csv'

        self.train_name = '../input/train/'
        self.test_name = '../input/test/'
        self.masks_write = '../input/train_y/'

    def rle_decode(self, mask_rle, shape=(768, 768)):
        """
        :param mask_rle: run-length as string formated (游程编码格式)
        :param shape: （height,width) of array to return
        :return:  numpu arr, 1 means mask, 0 means backgrount
        """
        s = mask_rle.split()  # 分割为list，偶数为坐标，奇数为长度
        starts, lengths = [np.asarray(x, dtype=int) for x in (s[0::2], s[1::2])]
        starts -= 1
        ends = starts + lengths    # i 开始， i+length-1 结束，
        img = np.zeros(shape[0] * shape[1], dtype=np.uint8)
        for l, r in zip(starts, ends):
            img[l:r] = 1
        res = img.reshape(shape).T  # why T?
        return res   # type np arr

    def rle_show(self):
        image_id = '0005d01c8.jpg'
        img = imread(image_id)
        masks = pd.read_csv(self.masks_name)
        img_masks = masks.loc[masks['ImageId'] == image_id, 'EncodedPixels'].tolist()
        # print(len(img_masks))
        de_masks = np.zeros(self.shape)
        for mask in img_masks:
            de_masks += self.rle_decode(mask, self.shape)

        fig, axarr = plt.subplots(1, 3, figsize=(15, 40))
        axarr[0].axis('off')
        axarr[1].axis('off')
        axarr[2].axis('off')
        axarr[0].imshow(img)
        axarr[1].imshow(de_masks)
        axarr[2].imshow(img)
        axarr[2].imshow(de_masks, alpha=0.4)
        plt.tight_layout(h_pad=0.1, w_pad=0.1)
        plt.show()

    def multi_process(self):
        masks = pd.read_csv(self.masks_name)
        num_masks = masks.shape[0]
        print('Total masks to decode = ', num_masks)
        clean_masks = masks.dropna()
        print('after dropna num to decode = ', clean_masks.shape[0])
        # im_id = set()
        count = 0
        for i in clean_masks.itertuples():
            if count > 100:
                break
            count += 1
            image_id = i.ImageId
            img_masks = clean_masks.loc[clean_masks['ImageId'] == image_id, 'EncodedPixels'].tolist()
            de_masks = np.zeros(self.shape)
            for mask in img_masks:
                de_masks += self.rle_decode(mask, self.shape)
            # np.save(self.masks_write + image_id + 'y', de_masks)
            io.imsave(self.masks_write + image_id + '_y.jpg', de_masks)

if __name__ == '__main__':
    A = PreProcess()
    time1 = time.time()
    # A.rle_show()
    A.multi_process()
    time2 = time.time()
    print("decode all masks cost: ", str(time2 - time1), 's')




