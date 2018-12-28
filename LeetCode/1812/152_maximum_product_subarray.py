# -*- coding: utf-8 -*-
# @StartTime : 2018/12/28 15:42
# @EndTime : 2018/9/12/28
# @Author  : Andy
# @Site    :
# @File    : 152_maximum_product_subarray.py
# @Software: PyCharm


"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        f = [None for i in range(len(nums))]
        g = [None for i in range(len(nums))]
        f[0] = nums[0]
        g[0] = nums[0]
        res = f[0]
        for i in range(1, len(nums)):
            f[i] = max(max(f[i-1] * nums[i], nums[i]), g[i-1] * nums[i])
            g[i] = min(min(f[i-1] * nums[i], nums[i]), g[i-1] * nums[i])
            res = max(res, f[i])
        return res


print Solution().maxProduct([2,-5,-2,-4,3])
