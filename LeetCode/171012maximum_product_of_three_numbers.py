# -*- coding: utf-8 -*-
# @StartTime : 10/12/2017 19:45
# @EndTime   : 10/12/2017 19:45
# @Author    : Andy
# @Site      : 
# @File      : 171012maximum_product_of_three_numbers.py
# @Software  : PyCharm

"""
Given an integer array, find three numbers whose product is maximum and
output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in
the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range
 of 32-bit signed integer.
"""


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        nums2 = sorted(nums)
        # return nums
        # 最大值有两种情况，数足够多的情况下，三个正，两个负数一个正数，
        #  数组元素过少的情况下（都是负数），最大的三个数相乘
        col = len(nums2)
        result1 = nums2[col-1] * nums2[col-2] * nums2[col-3]
        result2 = nums2[0] * nums2[1] * nums2[col-1]
        if result1 >= result2:
            return result1
        if result2 >result1:
            return result2



So = Solution()
print So.maximumProduct([-4,-3,-2,-1,60])


# class Solution(object):
#     def maximumProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # find three abs-max numbers and one fourth max number
#         max_abs1 = -1001
#         max_abs2 = -1001
#         max_abs3 = -1001
#         max_number4 = -1001
#         if len(nums) == 3:
#             return nums[0] * nums[1] *nums[2]
#         for i in range(len(nums)):
#             if abs(nums[i]) > max_abs3:
#                 temp = abs(nums[i])
#                 if temp > max_abs1:
#                     max_abs3 = max_abs2
#                     max_abs2 = max_abs1
#                     max_abs1 = nums[i]
#                 elif temp > max_abs2:
#                     max_abs3 = max_abs2
#                     max_abs2 = nums[i]
#                 else:
#                     max_abs3 = nums[i]
#                     if nums[i] > 0:
#                         max_number4 = nums[i]
#
#         for i in range(len(nums)):
#             if nums[i] > max_number4 and abs(nums[i]) < max_abs3:
#                 max_number4 = nums[i]
#         result = max_abs1 * max_abs2 * max_abs3
#         result1 = max_abs1 * max_abs2 * max_number4
#         result2 = max_abs1 * max_abs3 * max_number4
#         result3 = max_abs2 * max_abs3 * max_number4
#         max = result
#         if result1 > max:
#             return result1
#         if result2 > max :
#             return result2
#         if result3 > max :
#                 return result3
#         return max
