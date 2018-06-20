# -*- coding: utf-8 -*-
# @StartTime : 2018/6/19 21:13
# @EndTime : 2018/6/19 21:13
# @Author  : Andy
# @Site    : 
# @File    : 47_permutation_180619.py
# @Software: PyCharm


"""
Given a collection of numbers that might contain
 duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
Seen this question in a real interview before?  YesNo
Subscribe to see which companies asked this question.
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def dfs(nums, path):
            if not nums:
                if path not in res:
                    res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], path + [nums[i]])

        dfs(nums, [])
        return res


a = [1, 1, 2]
print(Solution().permuteUnique(a))