# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/3 16:40
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 010_rect_cover_180703.py
"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number < 1:
            return 0
        if number == 1:
            return 1
        res = [1, 2]
        for i in range(2, number):
            temp = res[-1] + res[-2]
            res.append(temp)
        return res[-1]