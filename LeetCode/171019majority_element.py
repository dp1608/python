# -*- coding: utf-8 -*-
# @StartTime : 10/18/2017 23:51
# @EndTime   : 10/18/2017 23:56
# @Author    : Andy
# @Site      : 
# @File      : 171019majority_element.py
# @Software  : PyCharm

"""
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always
 exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""
import collections

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = collections.Counter(nums)
        majority = c.most_common(1)
        return majority[0][0]

So = Solution()
print So.majorityElement([1,1,3,4,1])