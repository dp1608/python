# -*- coding: utf-8 -*-
# @StartTime : 11/5/2017 23:16
# @EndTime   : 11/5/2017 23:16
# @Author    : Andy
# @Site      : 
# @File      : 171105search_in_rotated_sorted_array.py
# @Software  : PyCharm

"""
Suppose an array sorted in ascending order is rotated at some pivot
unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its
index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def erfen(self,i,j,target):
            temp = (i + j) / 2
            if nums[temp] == target:
                return temp
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            if temp == i:
                return -1
            if nums[temp] < target:
                erfen(temp,j,target)
            else:
                erfen(i,temp,temp)

        min_index = 0
        max_index = len(nums) - 1
        if target <= nums[min_index]:
            while 1:
                middle = (min_index + max_index) / 2
                if nums[middle] > nums[0] and nums[middle] >= target:
                    self.erfen(min_index,middle,target)
                if nums[middle] > nums[0] and nums[middle] < target:














