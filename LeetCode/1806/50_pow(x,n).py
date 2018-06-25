# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/20 14:04
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 50_pow(x,n).py

"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def pow(x, n):
            positive = 1
            if n < 0:
                positive = 0
            if n == 0:
                return 1
            if n == 1:
                return x

            n = abs(n)
            res = pow(x, n >> 1)
            res *= res
            if n & 0x1:
                res *= x
            if not positive:
                return 1.0 / res
            return res

        return pow(x, n)


print(Solution()).myPow(-2.0, -3)