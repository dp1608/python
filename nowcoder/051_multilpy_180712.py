# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/12 14:41
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 051_multilpy_180712.py

"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
"""


# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if len(A) < 1:
            return []
        size = len(A)
        c = []
        d = []

        c.append(1)
        for i in range(1, size):
            c.append(A[i - 1] * c[-1])
        # print(c)
        d.append(1)
        for i in range(size - 2, -1, -1):
            d.append(A[i + 1] * d[-1])
        # print(d)
        d = d[::-1]
        b = []
        for i in range(size):
            b.append(c[i] * d[i])
        return b

print Solution().multiply([3,2,5,4])