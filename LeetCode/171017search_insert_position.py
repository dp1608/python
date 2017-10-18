# -*- coding: utf-8 -*-
# @StartTime : 10/17/2017 15:26
# @EndTime   : 10/17/2017 15:35
# @Author    : Andy
# @Site      : 
# @File      : 171017search_insert_position.py
# @Software  : PyCharm
"""
Given a sorted array and a target value, return the index if the target is
found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

"""
# 边界条件一定要多考虑啊！
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)

So = Solution()
print So.searchInsert([1,3,4,6],7)