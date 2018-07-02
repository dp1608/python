# -*- coding: utf-8 -*-
# @StartTime : 2018/5/8 20:15
# @EndTime : 2018/5/8 20:15
# @Author  : Andy
# @Site    : 
# @File    : 180508fisrt_missing_positive.py
# @Software: PyCharm

"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.


"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size_nums = len(nums)
        if size_nums < 1:
            return 1
        i = 0
        # for i in range(size_nums):
        while i < size_nums:
            if nums[i] < 1:
                i += 1
                continue
            elif nums[i] > size_nums:
                i += 1
                continue
            else:
                if nums[nums[i] - 1] == nums[i]:
                    i += 1
                    continue
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
                # i = i  1
        for i in range(size_nums + 1):
            if i == size_nums:
                return i + 1
            elif nums[i] != i + 1:
                return i + 1


So = Solution()
print(So.firstMissingPositive([3, 4, -1, 1]))


