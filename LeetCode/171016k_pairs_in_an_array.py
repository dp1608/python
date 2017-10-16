# -*- coding: utf-8 -*-
# @StartTime : 10/16/2017 10:32
# @EndTime   : 10/16/2017 10:47
# @Author    : Andy
# @Site      : 
# @File      : 171016k_pairs_in_an_array.py
# @Software  : PyCharm

"""
Given an array of integers and an integer k, you need to find the number of
unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

    Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique
pairs.
    Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4)
and (4, 5).
    Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
"""
import collections

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        res = 0
        c = collections.Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                res += 1
        return res



# 13mins costed
# Time Limit Exceeded
# class Solution(object):
#     def findPairs(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         count = 0
#         sort_reserve = sorted(nums)
#         success_reserve = []
#         for i in range(len(nums)):
#             j = i+1
#             while j < len(nums):
#                 if sort_reserve[i] + k == sort_reserve[j] and sort_reserve[i] \
#                         not in success_reserve:
#                     count += 1
#                     success_reserve.append(sort_reserve[i])
#                     break
#                 j += 1
#         return count

# Time Limit Exceeded
# Code wastes 15mins
# class Solution(object):
#     def findPairs(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         if k < 0:
#             return 0
#         count = 0
#         col = len(nums)
#         reserve = []
#         for i in range(col):
#             for j in range(col):
#                 if i != j and nums[j]+k == nums[i]:
#                    if nums[i] not in reserve:
#                        reserve.append(nums[i])
#                        count += 1
#                        break
#         return count
#
So = Solution()
print So.findPairs([3, 1, 4, 1, 5], 2)
print So.findPairs([1, 2, 3, 4, 5], k = 1)
print So.findPairs([1,2,3,4,5],-1)

#

