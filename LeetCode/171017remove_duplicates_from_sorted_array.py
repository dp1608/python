# -*- coding: utf-8 -*-
# @StartTime : 10/17/2017 14:19
# @EndTime   : 10/17/2017 14:29
# @Author    : Andy
# @Site      : 
# @File      : 171017remove_duplicates_from_sorted_array.py
# @Software  : PyCharm

"""
Given a sorted array, remove the duplicates in place such that each element
appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with
constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums
being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
"""

# 审题，边界，测试案例最好自己写。
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                del nums[i+1]
            if i < len(nums) - 1 and nums[i] != nums[i+1]:
                i += 1
        return len(nums)

So = Solution()
print So.removeDuplicates([1,1,2])
print So.removeDuplicates([1,1,1])