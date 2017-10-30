# -*- coding: utf-8 -*-
# @StartTime : 10/30/2017 15:22
# @EndTime   : 10/30/2017 15:22
# @Author    : Andy
# @Site      : 
# @File      : 171030three_sum_medium.py
# @Software  : PyCharm


"""
Given an array S of n integers, are there elements a, b, c in S
such that a + b + c = 0? Find all unique triplets in the array
which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

#Time Limit Exceeded
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in xrange(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1;
                    r -= 1
        return res


        # def sortabc(self,a,b,c):
        #     if a <= b and b <= c:
        #         return [a,b,c]
        #     if a <= c and c <= b:
        #         return [a, c, b]
        #     if b <= a and a <= c:
        #         return [b, a, c]
        #     if b <= c and c <= a:
        #         return [b, c, a]
        #     if c <= a and a <= b:
        #         return [c, a, b]
        #     if c <= b and b <= a:
        #         return [c, b, a]
        #
        # result = []
        # col = len(nums)
        # for i in range(col):
        #     for j in range(i+1, col):
        #         a = nums[i]
        #         b = nums[j]
        #         if (0 - a - b) in nums[j + 1:]:
        #             if sortabc(self,a,b,0 - a - b) not in result:
        #                 result.append(sortabc(self,a,b,0 - a - b))
        # return result

So = Solution()
print So.threeSum([-1, 0, 1, 2, -1, -4])
print So.threeSum([0, 0])
