# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/26 17:26
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 90_subsetsII_180626.py

"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

# class Solution(object):
#     def subsetsWithDup(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         if not nums:
#             return [[]]
#
#         start = nums[0]
#         res = [
#             [
#                 [], [start]
#             ]
#         ]
#
#         def add_one_num(number):
#             this = res[-1][:]
#             pre = [_ for _ in this]
#             size = len(this)
#             for i in range(size):
#                 this[i].append(number)
#             # this = pre + this
#             # this.append([])
#             this += pre
#             res.append(this)
#
#         for i in range(1, len(nums)):
#             add_one_num(nums[i])
#
#         return res[-1]


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        nums.sort()
        start = nums[0]
        res =[
                [], [start]
            ]

        def add_one_num(number, res):
            this = [i[:] for i in res]
            pre = [i[:] for i in res]
            size = len(this)
            for i in range(size):
                this[i].append(number)
            # this = pre + this
            # this.append([])
            for i in range(size):
                if pre[i] not in this:
                    this.append(pre[i])
            return this

        for i in range(1, len(nums)):
            res = add_one_num(nums[i], res)

        return res

nums = [1, 2, 2]
nums = [4,4,4,1,4]
print(Solution().subsetsWithDup(nums))
