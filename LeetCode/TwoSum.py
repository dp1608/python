# -*- coding: utf-8 -*-
# @Time    : 2017/4/6 22:42
# @Author  : Andy
# @E-mail  ：chendi@radi.ac.cn
# @Site    : 
# @File    : TwoSum.py
# @Software: PyCharm

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length_nums = len(nums)
        for i in range(0,length_nums-1):
            for j in range(i + 1,length_nums):
                if nums[i] + nums[j] == target:
                    temp = [i, j]
                    return temp
# class Solution(object):
#     def twoSum(self, nums, target):
#         if len(nums) <= 1:
#             return False
#         buff_dict = {}
#         for i in range(len(nums)):
#             if nums[i] in buff_dict:
#                 return [buff_dict[nums[i]], i]
#             else:
#                 buff_dict[target - nums[i]] = i
SUM=Solution()
print SUM.twoSum(nums=[3,2,4],target=6)


