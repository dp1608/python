# -*- coding: utf-8 -*-
# @StartTime : 10/18/2017 10:24
# @EndTime   : 10/18/2017 10:42
# @Author    : Andy
# @Site      : 
# @File      : 171018plus_one.py
# @Software  : PyCharm

"""
Given a non-negative integer represented as a non-empty array of digits,
plus one to the integer.

You may assume the integer do not contain any leading zero, except the number
 0 itself.

The digits are stored such that the most significant digit is at the head of
the list.
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        count = 0
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                break
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    count = 1
                continue
        if digits[0] == 0 and count == 1:
            digits.insert(0,1)
        if digits[0] == 0 and count == 0:
            digits[0] += 1
        return digits

So = Solution()
print So.plusOne([0])
print So.plusOne([9])
print So.plusOne([1,9])
print So.plusOne([9,9,9,9])