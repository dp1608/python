# -*- coding: utf-8 -*-
# @StartTime : 10/13/2017 13:58
# @EndTime   : 10/13/2017 14:45
# @Author    : Andy
# @Site      : 
# @File      : 171013find_all_numbers_disappered_in_an_array.py
# @Software  : PyCharm

"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2 = []
        for i in range(0,len(nums)):
            while nums[i] and nums[i] != i+1:
                if nums[nums[i]-1] == nums[i]:
                    nums[nums[i]-1] = 0
                temp = nums[nums[i]-1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
        for i in range(0,len(nums)):
            if nums[i] == 0:
                nums2.append(i+1)


        return nums2

So = Solution()
print So.findDisappearedNumbers([4,3,2,7,6,2,3,1])