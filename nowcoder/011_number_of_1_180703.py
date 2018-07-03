# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/3 16:44
# @End_time: 
# @Author  : Andy
# @Site    : https://www.cnblogs.com/cotyb/archive/2016/02/11/5186461.html
# @File    : 011_number_of_1_180703.py
"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        cnt = 0
        if n >= 0:
            while n:
                n = n & n - 1
                cnt += 1
        else:
            n = - n - 1
            while n:
                n = n & n - 1
                cnt += 1
            cnt = 32 - cnt
        return cnt

print(Solution().NumberOf1(-1))
