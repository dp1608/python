# -*- coding: utf-8 -*-
# @StartTime : 10/13/2017 12:15
# @EndTime   : 10/13/2017 12:49
# @Author    : Andy
# @Site      : 
# @File      : 171013max_consecutive_ones.py
# @Software  : PyCharm

"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        temp = 0
        i = 0
        while (i < len(nums)):
            while (nums[i] == 1):
                temp += 1
                i += 1
                if temp > count:
                    count = temp
                if i == len(nums):
                    return count
            temp = 0
            i += 1
        return count

So = Solution()
print So.findMaxConsecutiveOnes([1,0,1,1,0,1])
