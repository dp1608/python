# -*- coding: utf-8 -*-
# @StartTime : 2018/8/18 13:42
# @EndTime : 2018/8/18 16:45
# @Author  : Andy
# @Site    : https://www.kaggle.com/inversion/run-length-decoding-quick-start/notebook
# @File    : pre_process.py
# @Software: PyCharm


"""
This program is basic u-net using tensorflow, thanks to Vijay Jadhav.

"""


import os
import sys
import numpy as np
import tensorflow as tf
import random
import math
import warnings
import pandas as pd
import cv2
import matplotlib.pyplot as plt

from tqdm import tqdm
from itertools import chain
from skimage.io import imread, imshow, imread_collection, concatenate_images
from skimage.transform import resize
from skimage.morphology import label


IMG_WIDTH = 784
IMG_HEIGHT = 784
IMG_CHANNELS = 3
TRAIN_PATH = '../input/train/'
TRAIN_Y_PATH = '../input/train_y/'
TEST_PATH = '../input/test/'
BATCH_SIZE = 32


# take train to 7:3 ship 7:3 not ship 7:3 >> train 7:3
def split_train(all_ids, has_ship_ids):
    all_ids_set = set(all_ids)
    has_ship_ids_set = set(has_ship_ids)
    not_has_ship_ids_set = all_ids_set & has_ship_ids_set
    not_has_ship_ids = list(not_has_ship_ids_set)
    random.shuffle(has_ship_ids)
    random.shuffle(not_has_ship_ids)
    len1 = len(has_ship_ids)
    len2 = len(not_has_ship_ids)
    res_train_id = has_ship_ids[0:len1//10 * 7] + not_has_ship_ids[0:len2//10 * 7]
    res_test_id = has_ship_ids[len1//10 * 7:] + not_has_ship_ids[len2//10 * 7:]
    random.shuffle(res_train_id)
    random.shuffle(res_test_id)
    return res_train_id, res_test_id


# get IDs
# train_ids means all train img id
# train_y_ids means train img id which has ship
# test_ids means submission id
train_ids_pre = next(os.walk(TRAIN_PATH))[1]
train_y_ids_pre = next(os.walk(TRAIN_Y_PATH))[1]
# train_y_ids_pre_2 = []
# for i in range(len(train_y_ids_pre_1)):
#     train_y_ids_pre_2.append(train_y_ids_pre_1[i].split('_')[0] + '.jpg')

test_ids_post = next(os.walk(TEST_PATH))[1]
train_ids, test_ids = split_train(train_ids_pre, train_y_ids_pre)


# Get train images and masks
images = np.zeros((BATCH_SIZE, IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)
labels = np.zeros((BATCH_SIZE, IMG_HEIGHT, IMG_WIDTH, 1), dtype=np.bool)


X_train = images
Y_train = labels

# Get test iamges
X_test = np.zeros((BATCH_SIZE, IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)


def next_batch(batch_size, batch):
    global images, labels
    count = batch_size * batch
    train_id = train_ids[count: count + batch_size]
    for i in range(batch_size):
        images[i] = imread(TRAIN_PATH + train_id[i])
        labels[i] = imread(TRAIN_Y_PATH + train_id[i])
    return images, labels


# deconv
def deconv2d(input_tensor, filter_size, output_size, out_channels, in_channels, name, strides=[1, 1, 1, 1]):
    dyn_input_shape = tf.shape(input_tensor)
    batch_size = dyn_input_shape[0]
    out_shape = tf.stack([batch_size, output_size, output_size, out_channels])
    filter_shape = [filter_size, filter_size, out_channels, in_channels]
    w = tf.get_variable(name=name, shape=filter_shape)
    h1 = tf.nn.conv2d_transpose(input_tensor, w, out_shape, strides, padding='SAME')
    return h1


def conv2d(input_tensor, depth, kernel, name, strides=(1, 1), padding="SAME"):
    return tf.layers.conv2d(input_tensor, filters=depth, kernel_size=kernel, strides=strides,
                            padding=padding, activation=tf.nn.relu, name=name)


def max_pool(input_tensor, name, size=2, stride=2):
    return tf.nn.max_pool(input_tensor, ksize=[1, size, size, size],
                          strides=[1, stride, stride, 1],
                          name=name)


X = tf.placeholder(tf.float32, [BATCH_SIZE, IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS])
Y_ = tf.placeholder(tf.float32, [BATCH_SIZE, IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS])
lr = tf.placeholder(tf.float32)


# 768
c1 = conv2d(X, 8, 3, strides=(2, 2), name="conv1_1")     # 384 x 384 x 8
c1 = conv2d(c1, 8, 3, name="conv1_2")                    # 384 x 384 x 8
p1 = max_pool(c1, name='pool1')                          # 192 x 192 x 8


c2 = conv2d(c1, 16, 3, name='conv2_1', strides=(2, 2))   # 96 x 96 x 16
c2 = conv2d(c2, 16, 3, name='conv2_2')                   # 96 x 96 x 16
c2 = conv2d(c2, 16, 3, name='conv2_3')                   # 96 x 96 x 16
p2 = max_pool(c2, name='pool2')                          # 48 x 48 x 16

c3 = conv2d(c2, 32, 3, name='conv3_1')
c3 = conv2d(c3, 32, 3, name='conv3_2')                   # 48 x 48 x 32
c3 = conv2d(c3, 32, 3, name='conv3_3')                   # 48 x 48 x 32
p3 = max_pool(c3, name='pool2')                          # 24 x 24 x 32

c4 = conv2d(c3, 64, 3, name='conv4_1')                   # 24 x 24 x 64
c4 = conv2d(c4, 64, 3, name='conv4_2')                   # 24 x 24 x 64
c4 = conv2d(c4, 64, 3, name='conv4_3')                   # 24 x 24 x 64

c5 = conv2d(c4, 128, 3, name='conv5_1')
c5 = conv2d(c5, 128, 3, name='conv5_2')
c5 = conv2d(c5, 128, 3, name='conv5_3')                 # 24 x 24 x 128

d5 = deconv2d(c5, 1, 24, 128, 128, "deconv_1")          # 24 x 24 x 128
d5 = tf.nn.relu(d5)

d6 = deconv2d(d5, 2, 48, 64, 128, "deconv_2", strides=[1, 2, 2, 1])           # 48 x 48 x 64
d6 = tf.nn.relu(d6)

d7 = deconv2d(d6, 2, 96, 32, 64, "deconv_3", strides=[1, 2, 2, 1])            # 96 x 96 x 32
d7 = tf.nn.relu(d7)

d8 = deconv2d(d7, 2, 192, 16, 32, "deconv_4", strides=[1, 2, 2, 1])           # 192 x 192 x 16
d8 = tf.nn.relu(d8)

d9 = deconv2d(d8, 2, 384, 8, 16, "deconv_5", strides=[1, 2, 2, 1])            # 384 x 384 x 8
d9 = tf.nn.relu(d9)

d10 = deconv2d(d9, 2, 768, 8, 8, "deconv_6", strides=[1, 2, 2, 1])            # 768 x 768 x 8
d10 = tf.nn.relu(d10)

logits = deconv2d(d10, 1, 768, 1, 8, "logits")           # 768 x 768 x 1

loss = tf.losses.sigmoid_cross_entropy(Y_, logits)
optimizer = tf.train.AdamOptimizer(lr).minimize(loss)


# init
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

batch_count = 0
display_count = 1
for i in range(10000):
    if batch_count > 1000:
        batch_count = 0

    batch_X, batch_Y = next_batch(BATCH_SIZE, batch_count)
    batch_count += 1
    feed_dict = {X: batch_X, Y_: batch_Y, lr: 0.0005}
    loss_value, _ = sess.run([loss, optimizer], feed_dict=feed_dict)

    if i % 500 == 0:
        print(str(display_count) + "training loss:", str(loss_value))
        display_count += 1
print("done")





















