# -*- coding: utf-8 -*-
# @StartTime : 2018/5/19 19:29
# @EndTime : 2018/5/19 19:29
# @Author  : Andy
# @Site    : 
# @File    : 180519subsets.py
# @Software: PyCharm

"""

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)


# # Bit Manipulation
# def subsets2(self, nums):
#     res = []
#     nums.sort()
#     for i in xrange(1 << len(nums)):
#         tmp = []
#         for j in xrange(len(nums)):
#             if i & 1 << j:  # if i >> j & 1:
#                 tmp.append(nums[j])
#         res.append(tmp)
#     return res
#
#
# # Iteratively
# def subsets(self, nums):
#     res = [[]]
#     for num in sorted(nums):
#         res += [item + [num] for item in res]
#     return res

num = [1,2,3]
print(Solution().subsets(num))