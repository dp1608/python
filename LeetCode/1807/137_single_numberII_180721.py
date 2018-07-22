# -*- coding: utf-8 -*-
# @StartTime : 2018/7/21 21:59
# @EndTime : 2018/7/21 21:59
# @Author  : Andy
# @Site    : 
# @File    : 137_single_numberII_180721.py
# @Software: PyCharm

"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once.
Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        single_dict = {}
        for i in range(len(nums)):
            if nums[i] not in single_dict.keys():
                single_dict[nums[i]] = 1
            else:
                single_dict[nums[i]] += 1
        for num in single_dict:
            if single_dict[num] != 3:
                return num

print(Solution().singleNumber([2,2,3,2]))