# -*- coding: utf-8 -*-
# @StartTime : 2018/8/17 13:23
# @EndTime : 2018/8/17 13:23
# @Author  : Andy
# @Site    : 
# @File    : test.py
# @Software: PyCharm

# s = [11111,2,222222,3,444444,5,111111111,5,123124,3,123151,4]
# for x in (s[0:][::2], s[1:][::2]):
#     print(x)
#
# for x in (s[0::2], s[1::2]):
#     print(x)

import numpy as np
import pandas as pd
# df = pd.DataFrame([[1, 1], [4, 5]])
#
# for row in df.itertuples():
#     print(row)



# img = np.zeros(5 * 5, dtype=int)
# img[1:5] = 1
# print(img)
# res = img.reshape((5,5))
# rest = img.reshape((5,5)).T
# print(res)
# print(rest)


# masks = pd.read_csv('test.csv')
# num_masks = masks.shape[0]
# print('Total masks to decode = ', num_masks)
# cleaned = masks.dropna()
# for i in cleaned.itertuples():
#     # print(type(i.ImageId))
#     img_masks = masks.loc[masks['ImageId'] == i.ImageId, 'EncodedPixels'].tolist()
#     # map(str, img_masks)
#     if img_masks[0] == np.nan:
#         print('!!!!')
#         continue
#     print(type(img_masks[0]))
#     print(img_masks[0])
#

    # if not i.EncodedPixels.split():
        # print(i.ImageId)
    # else:
    #     print(i.EncodedPixels)
# s = set([1,2,3,4,'4'])
# s.add('1234')
# print(s)
from skimage import  io

# a = np.load('008be7e31.jpgy.npy')
# print(a.dtype)
# print(a.shape)
# print(a)
# uint8-46k
# aa = pd.DataFrame(a)
# aa.to_csv('008be7e31.csv')
# np.savetxt('test', a)
# io.imsave('xincwenjian.jpg', a)

train_y_ids_pre_1 = ['12314_y.jgp', '12312351223_y.jpg']
train_y_ids_pre_2 = []
for i in range(len(train_y_ids_pre_1)):
    train_y_ids_pre_2.append(train_y_ids_pre_1[i].split('_')[0] + '.jpg')
print(train_y_ids_pre_2)