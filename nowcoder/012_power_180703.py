# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/3 17:17
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 012_power_180703.py

"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
"""

# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        positive = True
        if not exponent:
            return 1
        if exponent < 0:
            exponent = -exponent
            positive = False

        res = 1
        i = 1
        temp = base
        while exponent:
            if i <= exponent:
                res *= temp
                temp = temp * temp
                exponent -= i
                i = i << 1
            else:
                temp = base
                i = 1
        if positive:
            return res
        else:
            return 1 / res

print(Solution().Power(2, 11))