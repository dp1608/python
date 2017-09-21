# -*- coding: utf-8 -*-
# @StartTime : 9/21/2017 22:14
# @EndTime   : 9/21/2017 22:14
# @Author    : Andy
# @Site      : 
# @File      : test_for_ideas.py
# @Software  : PyCharm

temp='abcde'
print temp[4]
revers=''
for j in range(len(temp) - 1, -1, -1):
    revers = revers[:len(temp) - j - 1] + temp[j]
# print revers

temp2='What a pity it is!'
print len(temp2)