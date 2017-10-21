# -*- coding: utf-8 -*-
# @StartTime : 10/19/2017 10:47
# @EndTime   : 10/19/2017 10:47
# @Author    : Andy
# @Site      : 
# @File      : 171019contains_duplicateII.py
# @Software  : PyCharm

"""
Given an array of integers and an integer k, find out whether there are two
distinct indices i and j in the array such that nums[i] = nums[j] and the
absolute difference between i and j is at most k.
"""
# dictionary and enumerat's application.
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False




# #Time Limit Exceeded
# class Solution(object):
#     def containsNearbyDuplicate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         if len(nums) < 2 or k == 0:
#             return False
#         for i in range(len(nums)):
#             for j in range(min(len(nums), i + k), i, -1):
#                 if nums[i] == nums[j]:
#                     return True
#         return False



So = Solution()
print So.containsNearbyDuplicate([-1, -1], 1)