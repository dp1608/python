# -*- coding: utf-8 -*-
# @StartTime : 10/20/2017 22:48
# @EndTime   : 10/20/2017 22:48
# @Author    : Andy
# @Site      : 
# @File      : 171020missing_number.py
# @Software  : PyCharm

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?

Credits:
Special thanks to @jianchao.li.fighter for adding
this problem and creating all test cases.
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, v in enumerate(nums):
            if i != v:
                return i
        return len(nums)


So = Solution()
print So.missingNumber([0,1,2,3,5])