# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/25 13:00
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 69_sqrt_x_180625.py

"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return 0
        if x < 0:
            return -1
        start = 1
        for i in range(((len(str(x)) + 1) // 2) - 1):
            start = start * 10
        end = start * 10

        def erfen(target, start, end):
            temp = start + end
            temp = temp // 2
            if temp * temp <= target and (temp + 1) * (temp + 1) > target:
                return temp
            elif temp * temp < target:
                return erfen(target, temp + 1, end)
            else:
                return erfen(target, start, temp - 1)

        res = erfen(x, start, end)
        return res

        # res = x >> ((len(str(x)) + 1) // 2)
        # count = res
        # while 1:
        #     if res * res <= x and (res + 1) * (res + 1) > x:
        #         return res
        #     if res * res > x:
        #         res = res - count
        #         count = 1
        #         continue
        #     res = res + count
        #     count = count << 1

        # while 1:
        #     if res * res <= x and (res + 1) * (res + 1) > x:
        #         return res
        #     res += 1


print(Solution().mySqrt(888))
print(Solution().mySqrt(8))
print(Solution().mySqrt(277568629))

print(Solution().mySqrt(2118751050))