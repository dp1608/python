# -*- coding: utf-8 -*-
# @StartTime : 10/17/2017 15:17
# @EndTime   : 10/17/2017 15:23
# @Author    : Andy
# @Site      : 
# @File      : 171017remove_element.py
# @Software  : PyCharm
"""
Given an array and a value, remove all instances of that value in place and
return the new length.

Do not allocate extra space for another array, you must do this in place
with constant memory.

The order of elements can be changed. It doesn't matter what you leave
beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of
nums being 2.
"""

# usage of continue in a loop is very important
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # nums.remove(val)
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                continue
            if nums[i] != val:
                i += 1
        return len(nums)


So = Solution()
print So.removeElement([3,2,2,3],3)

