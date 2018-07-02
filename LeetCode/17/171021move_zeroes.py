# -*- coding: utf-8 -*-
# @StartTime : 10/21/2017 14:17
# @EndTime   : 10/21/2017 14:25
# @Author    : Andy
# @Site      : 
# @File      : 171021move_zeroes.py
# @Software  : PyCharm

"""
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums
should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating
all test cases.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        col = len(nums)
        i = 0
        while i < col :
            if nums[i] == 0:
                del nums[i]
                col -= 1
                nums.append(0)
                continue
            i += 1

        print nums

So = Solution()
So.moveZeroes([0, 1, 0, 3, 12])
