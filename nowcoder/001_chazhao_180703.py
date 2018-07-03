# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/3 15:06
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 001_chazhao_180703.py
"""
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


1 2
3 5
6 7
"""

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not array:
            return False

        row = len(array)
        col = len(array[0])

        i = row - 1
        j = 0
        while i >= 0 and j <= col - 1:
            if target == array[i][j]:
                return True
            if target > array[i][j]:
                j += 1
                continue
            if target < array[i][j]:
                i -= 1
                continue
        return False


