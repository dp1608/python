# -*- coding: utf-8 -*-
# @StartTime : 10/18/2017 16:48
# @EndTime   : 10/18/2017 16:48
# @Author    : Andy
# @Site      : 
# @File      : 171018two_sumII.py
# @Software  : PyCharm

"""
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that
they add up to the target, where index1 must be less than index2.
 Please note that your returned answers (both index1 and index2) are
 not zero-based.

You may assume that each input would have exactly one solution and you
may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

# binary tree
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(numbers) < 2:
            return []
        left = 0
        right = len(numbers)-1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right -= 1
            else:
                left += 1






So = Solution()
print So.twoSum([2, 7, 11, 15], 9)
print So.twoSum([2, 3, 4], 6)