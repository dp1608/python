# -*- coding: utf-8 -*-
# @StartTime : 10/11/2017 16:25
# @EndTime   : 10/11/2017 16:40
# @Author    : Andy
# @Site      : 
# @File      : 171011contains_duplicate.py
# @Software  : PyCharm

"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the
array, and it should return false if every element is distinct.
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nums2 = list(set(nums))
        if len(nums) == len(nums2):
            return False
        else:
            return True



# # Time Limit Exceeded
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         col = len(nums)
#         for i in range(col):
#             for j in range(i+1,col):
#                 if nums[i] == nums[j]:
#                     return True
#
#         return False
#

So = Solution()
result = So.containsDuplicate(nums=[1,2,3,4,5])
print result