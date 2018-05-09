# -*- coding: utf-8 -*-
# @StartTime : 2018/5/8 15:20
# @EndTime : 2018/5/8 20:15
# @Author  : Andy
# @Site    : 
# @File    : 180503combination_sum_II.py
# @Software: PyCharm

"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in
candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


# class Solution(object):
#     def combinationSum2(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         result = []
#         candidates.sort()
#         # size_arr = len(candidates)
#
#         def in_combination(nums, target, curr, i):
#             if target == 0:
#                 if curr not in result:
#                     result.append(list(curr))
#                     return
#             if i >= len(nums):
#                 return
#             if nums[i] > target:
#                 if len(curr) > 0:
#                     temp = curr.pop()
#                     in_combination(nums, target + temp, curr, i)
#                 else:
#                     return
#             else:
#                 curr.append(nums[i])
#                 in_combination(nums, target - nums[i], curr, i + 1)
#         for j in range(len(candidates)):
#             in_combination(candidates, target, [], j)
#         return result
# 问题所在： candidates = [4,1,1,4,4,4,4,2,3,5] target = 10 时， 输出结果不正确 关键症结未找到

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        # size_arr = len(candidates)

        def in_combination(nums, target, curr, i):
            if target == 0:
                if curr not in result:
                    result.append(list(curr))
                    return
            for jj in range(i, len(nums)):
                if jj > i and nums[jj] == nums[jj - 1]:
                    continue
                if nums[jj] > target:
                    break
                in_combination(nums, target - nums[jj], curr+[nums[jj]], jj + 1)

        in_combination(candidates, target, [], 0)
        return result


So = Solution()
# candidates = [10, 1, 2, 7, 6, 1, 5]
# target = 8
candidates = [4,1,1,4,4,4,4,2,3,5]
target = 10
print(So.combinationSum2(candidates, target))