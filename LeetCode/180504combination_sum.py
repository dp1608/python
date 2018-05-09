# -*- coding: utf-8 -*-
# @StartTime : 2018/5/4 9:37
# @EndTime : 2018/5/4 9:37
# @Author  : Andy
# @Site    : 
# @File    : 180504combination_sum.py
# @Software: PyCharm

"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


# class Solution(object):
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#
#         if target == 0:
#             return []
#         size_candidates = len(candidates)
#         if 'a' not in locals().keys():
#             global a
#             a = [[] for jj in range(target)]
#         temp_arr = []
#         for i in range(size_candidates - 1, -1, -1):
#             temp_arr = []
#             temp = target - candidates[i]
#             if candidates[i] > target:
#                 continue
#             elif candidates[i] < target:
#                 if a[temp - 1] == []:
#                     temp_arr = (self.combinationSum(candidates[0:i], temp))
#                     temp_arr_len = len(temp_arr)
#                     for j in range(temp_arr_len):
#                         temp_arr[j].append(temp)
#                 else:
#                     temp_arr = a[temp - 1]
#                     temp_arr_len = len(temp_arr)
#                     for j in range(temp_arr_len):
#                         temp_arr[j].append(temp)
#             else:
#                 temp_arr.append([target])
#             a[target - 1] = temp_arr
#         return temp_arr"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()

        def com(nums, target, i, cur):
            if i == len(nums):
                return
            if target == 0:
                res.append(list(cur))
                return
            if nums[i] <= target:
                cur.append(nums[i])
                com(nums, target - nums[i], i, cur)
                cur.pop()
                com(nums, target, i + 1, cur)
            # else:
            #     com(nums, target, i + 1, cur)

        com(candidates, target, 0, [])
        return res



# a = [0 for i in range(100)]
# print(len(a[0:50]))
So = Solution()
candidates = [2, 3, 5]
target = 8
print(So.combinationSum(candidates, target))