# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/3 16:16
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 007_fibonacci_180703.py

"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
"""

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return 1
        res = []
        res += [1,1]
        for i in range(2, n):
            temp = res[-1] + res[-2]
            res.append(temp)
        # print(res)
        return res[-1]

print(Solution().Fibonacci(39))