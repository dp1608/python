# -*- coding: utf-8 -*-
# @StartTime : 10/17/2017 15:39
# @EndTime   : 10/17/2017 15:39
# @Author    : Andy
# @Site      : 
# @File      : 171017maximum_subarray.py
# @Software  : PyCharm
"""
Find the contiguous subarray within an array (containing at least one number)
 which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

# #
# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        # A wrong try 1
        # if len(nums) == 1:
        #     return nums[0]
        # count = [0 for col in range(len(nums))]
        # count[0] = nums[0]
        # for i in range(1,len(nums)):
        #     count[i] = count[i-1] + nums[i]
        # return max(count) - min(min(count),0)

        # Time Limit Exceeded 2
        # count = [0 for col in range(len(nums))]
        # count[0] = nums[0]
        # max_sub = nums[0]
        # for i in range(1,len(nums)):
        #     count[i] = count[i-1] + nums[i]
        # for i in range(len(nums)):
        #     if count[i] > max_sub:
        #         max_sub = count[i]
        #
        #     for j in range(i+1,len(nums)):
        #         sum_sub = count[j] - count[i]
        #         if sum_sub > max_sub:
        #             max_sub = sum_sub
        #         if count[i] > max_sub:
        #             max_sub = count[i]
        # return max_sub

        #third try
        # count = [0 for col in range(len(nums))]
        # count[0] = nums[0]
        # max_sub = nums[0]
        # for i in range(1,len(nums)):
        #     count[i] = count[i-1] + nums[i]
        # for i in range(len(nums)):
        #     if count[i] > max_sub:
        #         max_sub = count[i]
        #     if i+1 < len(nums):
        #         sum_sub = max(count[i+1:]) - count[i]
        #         if sum_sub > max_sub:
        #             max_sub = sum_sub
        # return max_sub


class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum


So = Solution()
print So.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print So.maxSubArray([1,2,3])
print So.maxSubArray([-2,-1])
print So.maxSubArray([0])