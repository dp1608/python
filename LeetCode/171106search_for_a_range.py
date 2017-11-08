# -*- coding: utf-8 -*-
# @StartTime : 2017年11月8日19:40:01
# @EndTime   : 2017年11月8日19:54:09
# @Author    : Andy
# @Site      : 
# @File      : 171106search_for_a_range.py
# @Software  : PyCharm


"""
Given an array of integers sorted in ascending order, find the starting and
ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        col = len(nums)
        if col <= 0 :
            return [-1, -1]
        min_index = 0
        max_index = col - 1

        def search_target(self, min_index, max_index, target):
            middle = (min_index + max_index) / 2
            if nums[middle] == target:
                return middle
            if nums[min_index] == target:
                return min_index
            if nums[max_index] == target:
                return max_index
            if min_index >= max_index - 1:
                return -1
            if nums[middle] < target:
                return search_target(self, middle, max_index, target)
            if nums[middle] > target:
                return search_target(self, min_index, middle, target)
        origin = search_target(self, min_index, max_index, target)
        end = origin
        if origin == -1:
            return [-1, -1]
        else:
            while origin - 1 >= 0 and nums[origin] == nums[origin - 1]:
                origin -= 1
            while end + 1 <= col - 1 and nums[end] == nums[end + 1]:
                end += 1
        return [origin, end]

So = Solution()
print So.searchRange( [5, 7, 7, 8, 8, 10],8)
print So.searchRange( [],0)
print So.searchRange( [0],0)
print So.searchRange( [5, 7, 7, 8, 8, 10],9)
print So.searchRange( [5, 7, 7, 8, 8, 10],10)
print So.searchRange( [5, 7, 7, 8, 8, 10],5)
print So.searchRange( [5, 7, 7, 8, 8, 10],7)