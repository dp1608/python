# -*- coding: utf-8 -*-
# @StartTime : 10/31/2017 15:06
# @EndTime   : 10/31/2017 16:51
# @Author    : Andy
# @Site      : 
# @File      : 171031four_sum_medium.py
# @Software  : PyCharm


"""
Given an array S of n integers, are there elements a, b, c, and d in S such
that a + b + c + d = target? Find all unique quadruplets in the array which
 gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[
                -1] * N:  # early termination
                return
            if N == 2:  # two pointers solve sorted 2-sum problem
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:  # recursively reduce N
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                        findNsum(nums[i + 1:], target - nums[i], N - 1,
                                 result + [nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results

        # # Time limit exceeded
        # nums.sort()
        # res = []
        # col = len(nums)
        # for a in range(col - 3):
        #     for b in range(a + 1, col - 2):
        #         for c in range(b + 1, col - 1):
        #             if target - nums[a] - nums[b] - nums[c] in nums[c + 1:] \
        #                     and [nums[a], nums[b], nums[c], target - nums[a] -
        #                             nums[b] - nums[c]] not in res:
        #                 res.append([nums[a], nums[b], nums[c], target -
        #                             nums[a] - nums[b] - nums[c]])
        # return res




        ## wrong answer
        # nums.sort()
        # res = []
        # for a in range(len(nums) - 3):
        #     for b in range(a + 1, len(nums) - 2):
        #         c = b + 1
        #         d = len(nums) - 1
        #         sum = nums[a] + nums[b] + nums[c] + nums[d]
        #         if target - sum == 0 and [nums[a], nums[b], nums[c],nums[d]]\
        #                 not in res:
        #             res.append([nums[a], nums[b], nums[c], nums[d]])
        #         while sum - target <= 0 and c < d - 1:
        #             c += 1
        #             sum = nums[a] + nums[b] + nums[c] + nums[d]
        #             if target - sum == 0 and [nums[a], nums[b], nums[c],
        #                                       nums[d]] not in res:
        #                 res.append([nums[a], nums[b], nums[c], nums[d]])
        #         while sum - target >= 0 and d > c + 1:
        #             d -= 1
        #             sum = nums[a] + nums[b] + nums[c] + nums[d]
        #             if target - sum == 0 and [nums[a], nums[b], nums[c], nums[d]] \
        #                     not in res:
        #                 res.append([nums[a], nums[b], nums[c], nums[d]])
        #
        # return res

So = Solution()
# print So.fourSum([1, 0, -1, 0, -2, 2], 0)
print So.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0)



