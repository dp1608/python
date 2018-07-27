# -*- coding: utf-8 -*-
# @StartTime : 2018/7/21 21:49
# @EndTime : 2018/7/21 21:49
# @Author  : Andy
# @Site    : 
# @File    : 136_single_number)180721.py
# @Software: PyCharm

"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]

        return res

print(Solution().singleNumber([2,2,1]))
print(2 & 2)