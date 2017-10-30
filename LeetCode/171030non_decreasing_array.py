# -*- coding: utf-8 -*-
# @StartTime : 10/30/2017 10:34
# @EndTime   : 10/30/2017 12:07
# @Author    : Andy
# @Site      : 
# @File      : 171030non_decreasing_array.py
# @Software  : PyCharm


"""
Given an array with n integers, your task is to check if it could become
non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for
every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first
4
 to
1
 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def nodecreasing(self, lista):
            for i in range(len(lista) - 1):
                if lista[i] > lista[i + 1]:
                    return False
            return True
        if nodecreasing(self, nums):
            return True
        else:
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    temp = nums[i]
                    nums[i] = nums[i + 1]
                    if nodecreasing(self, nums):
                        return True
                    nums[i] = temp
                    nums[i + 1] = temp
                    if nodecreasing(self, nums):
                        return True
                    else:
                        return False






        # counter = 0
        # i = 0
        # while i < len(nums) - 1:
        #     if nums[i] <= nums[i + 1]:
        #         i += 1
        #     else:
        #         counter += 1
        #         temp = nums[i]
        #         del nums[i]
        #         while i > 0 and nums[i] <= nums[i-1]:
        #             del nums[i]
        #             i = i - 1
        #         i = max(i - 1,0)
        #
        #     if counter >= 2:
        #         return False
        # return True


        # for i in range(len(nums) - 1):
        #     if nums[i] <= nums[i + 1]:
        #         continue
        #     else:
        #         counter += 1
        # if counter<= 1:
        #     return True
        # else:
        #     return False    [3,4,2,3]

So = Solution()
print So.checkPossibility([4,2,3])
print So.checkPossibility([3,4,2,3])
print So.checkPossibility([2,3,3,2,3])
print So.checkPossibility([1,2,4,5,3])
print So.checkPossibility([4,2,1])