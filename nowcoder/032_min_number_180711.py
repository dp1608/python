# -*- coding: utf-8 -*-
# @StartTime : 2018/7/11 22:20
# @EndTime : 2018/7/11 22:20
# @Author  : Andy
# @Site    : 
# @File    : 032_min_number_180711.py
# @Software: PyCharm

"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""

# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return
        str_numbers = map(str, numbers)
        str_numbers.sort(cmp=lambda x,y:cmp(x + y,y + x))
        # str_numbers = str_numbers[::-1]
        return "".join(str_numbers).strip('0') or '0'

a = [3,32,321,2,33]
print Solution().PrintMinNumber(a)