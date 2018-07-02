# -*- coding: utf-8 -*-
# @StartTime : 8/1/2017 20:16
# @EndTime   : 8/1/2017 20:16
# @Author    : Andy
# @Site      : 
# @File      : HammingDistance.py
# @Software  : PyCharm

"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
Note:
0 ≤ x, y < 2^31.
Example:
Input: x = 1, y = 4
Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ?   ?
The above arrows point to positions where the corresponding bits are different.
"""


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z=x^y
        c=0
        while z>0:
            z=z&(z-1)
            c=c+1
        return c



T=Solution()
t=T.hammingDistance(1,4)
print t