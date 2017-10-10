# -*- coding: utf-8 -*-
# @StartTime : 10/10/2017 22:09
# @EndTime   : 10/10/2017 22:09
# @Author    : Andy
# @Site      : 
# @File      : 171010rotate_array.py
# @Software  : PyCharm

"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to
[5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different
ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?
Related problem: Reverse Words in a String II

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        nums2 = [None for col in range(n)]
        for i in range(n):
            if n-k+i < n:
                nums2[i] = nums[n-k+i]
            else:
                nums2[i] = nums[i-k]

        nums[:] = nums2[:]

So = Solution()
nums = [1,2]
k = 1
So.rotate(nums,k)
print nums
