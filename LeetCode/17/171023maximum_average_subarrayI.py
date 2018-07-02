# -*- coding: utf-8 -*-
# @StartTime : 10/23/2017 16:09
# @EndTime   : 10/23/2017 16:09
# @Author    : Andy
# @Site      : 
# @File      : 171023maximum_average_subarrayI.py
# @Software  : PyCharm

"""
Given an array consisting of n integers, find the contiguous subarray
of given length k that has the maximum average value. And you need to output
the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        P = [0]

        for num in nums:
            P.append(P[-1] + num)

        max_k = max(P[i + k] - P[i]
                    for i in range(0,len(nums)- k + 1))

        return max_k / float(k)









# : Time Limit Exceeded
# class Solution(object):
#     def findMaxAverage(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: float
#         """
#         i = 0
#         max_num = nums[0]
#         temp = 0
#         min_num = 0
#         while i < len(nums) - k + 1:
#             if min_num > nums[i]:
#                 i += 1
#                 continue
#             temp = sum(nums[i:i + k])
#             min_num = min(nums[i:i + k])
#             if temp > max_num:
#                 max_num = temp
#             i += 1
#         # return max
#         return float(max_num) / k


So = Solution()
print So.findMaxAverage( [1,12,-5,-6,50,3], k = 4)