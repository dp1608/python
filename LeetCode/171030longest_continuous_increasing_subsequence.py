# -*- coding: utf-8 -*-
# @StartTime : 10/30/2017 12:46
# @EndTime   : 10/30/2017 12:51
# @Author    : Andy
# @Site      : 
# @File      : 171030longest_continuous_increasing_subsequence.py
# @Software  : PyCharm


"""
Given an unsorted array of integers, find the length of longest continuous
increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5],
its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a
 continuous one where 5 and 7 are separated by 4.
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its
length is 1.
"""


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter_max = 1
        counter = 1
        i = 0
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        while i < len(nums) - 1:
            if nums[i] < nums[i + 1]:
                counter += 1
                i += 1
            else:
                counter_max = max(counter_max, counter)
                counter = 1
                i += 1
        counter_max = max(counter_max, counter)
        return counter_max

So = Solution()
print So.findLengthOfLCIS([1,3,5,4,7])
print So.findLengthOfLCIS([2,2,2,2,2])
print So.findLengthOfLCIS([])