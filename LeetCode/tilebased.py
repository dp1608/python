# -*- coding: utf-8 -*-
# @StartTime : 11/14/2017 9:38
# @EndTime   : 11/14/2017 10:41
# @Author    : Andy
# @Site      : 
# @File      : tilebased.py
# @Software  : PyCharm
import math


temp = input("input i:")
i = int(temp)
temp = input("input j:")
j = int(temp)

# n xiangguan
temp_n11 = (i / 2)
temp_n1 = temp_n11 / 2.0
temp_n2 = i % 2
temp_n3 = 0
A = int(math.log(i + 1 , 2)) + 1
for xx in range(2, A):
    temp_n31 = i / (2 ** xx)
    temp_n32 = temp_n31 / (2 ** xx * 1.0)
    temp_n3 += temp_n32
temp_n3 =  temp_n3 * 3
temp_n = temp_n1 + temp_n2 - temp_n3
#
temp_i1 = j + (i % 2) * (-3 / 2.0 * j + (j % 2) * 1.5)
temp_i21 = math.log((i+1) / 4.0, 2)
if temp_i21 <=0:
    temp_i21 = 0.1
temp_i22 = math.floor(math.floor(temp_i21) / math.ceil(temp_i21))
temp_i23 = int(j / (i + 1))
temp_i2 = temp_i22 * temp_i23 * 3
temp_i = temp_i1 - temp_i2
res = str(temp_n) + '*n+ ' + str(int(temp_i))

print res

