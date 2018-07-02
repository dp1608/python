# -*- coding: utf-8 -*-
# @StartTime : 10/16/2017 16:35
# @EndTime   : 10/16/2017 16:35
# @Author    : Andy
# @Site      : 
# @File      : 171016degree_of_an_array.py
# @Software  : PyCharm

"""
Given a non-empty array of non-negative integers nums, the degree of this
 array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray
    of nums, that has the same degree as nums.

    Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

    Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""
import collections


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = collections.Counter(nums)
        first, last = {}, {}
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            last[v] = i
        degree = max(c.values())
        return min(last[v] - first[v] + 1 for v in c if c[v] == degree)
# class Solution(object):
#     def findShortestSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         dict_nums = collections.Counter(nums)
#
#         # col = len(nums)
#         if len(nums) == 1:
#             return 1
#         def distance(self, value):
#             first_index = nums.index(value)
#             for j in range(len(nums)-1,-1,-1):
#                 if nums[j] == value:
#                     end_index = j
#                     return end_index-first_index
#             return 0
#
#         most_common = dict_nums.most_common(2)
#         if len(most_common) == 1:
#             return most_common[0][1]
#         # find the number of the max elements
#         count_1 = most_common[0][1]  # which means frequency
#         count_2 = most_common[1][1]
#
#         while count_1 == count_2:
#             distance1 = distance(self,most_common[0][0])
#             distance2 = distance(self,most_common[1][0])
#             if distance1 <= distance2:
#                 dict_nums.pop(most_common[1][0])
#             else:
#                 dict_nums.pop(most_common[0][0])
#             most_common = dict_nums.most_common(2)
#             count_1 = most_common[0][1]
#             if len(most_common) == 1:
#                 break
#             count_2 = most_common[1][1]
#
#         distanceend = distance(self,most_common[0][0])
#         return distanceend+1

So = Solution()
print So.findShortestSubArray([1,2,2,3,1])
print So.findShortestSubArray([1,2,2,3,1,4,2])