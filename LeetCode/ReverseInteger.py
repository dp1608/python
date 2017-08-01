# -*- coding: utf-8 -*-
# @StartTime : 2017/7/18 9:55
# @EndTime   : 2017/7/18 10:42
# @Author    : Andy
# @Site      : 
# @File      : ReverseInteger.py
# @Software  : PyCharm
import  sys

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        mark=0
        if x<0:
            stringX=str(-x)
            mark=1
        else:
            stringX=str(x)
        stringY=""
        for i in reversed(stringX):
            stringY+=i
        y=int(stringY)
        if y>0xfffffffff/2:
            return 0
        else:
            if mark:
                return -y
            else:
                return y





a=Solution()
print a.reverse(-123)
