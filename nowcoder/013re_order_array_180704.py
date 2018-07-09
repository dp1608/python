# -*- coding: utf-8 -*-
# @StartTime : 2018/7/4 9:34
# @EndTime : 2018/7/4 9:34
# @Author  : Andy
# @Site    : 
# @File    : 013re_order_array_180704.py
# @Software: PyCharm
"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        res1 = []
        res2 = []
        for i in range(len(array)):
            if array[i] & 0x1:
                res1.append(array[i])
            else:
                res2.append(array[i])
        return res1 + res2

a = [1,2,3,4,5]
print(Solution().reOrderArray(a))