# -*- coding: utf-8 -*-
# @StartTime : 2018/6/15 10:49
# @EndTime : 2018/6/15 10:49
# @Author  : Andy
# @Site    : 
# @File    : 46_permutations_180615.py
# @Software: PyCharm

"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 1:
            return []
        res = []
        # size = len(nums)

        def dfs(nums, path):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], path + [nums[i]])

        # for i in range(size):
        dfs(nums, path=[])
        return res

print(Solution().permute([1,2,3]))
# a = [1, 2]
# print a + a[:0] + a[1:]


