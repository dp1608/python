# -*- coding: utf-8 -*-
# @StartTime : 2018/8/26 11:00
# @EndTime : 2018/8/26 11:00
# @Author  : Andy
# @Site    : 
# @File    : 45_jump_gameII_180826.py
# @Software: PyCharm


"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.

"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        if len(nums) < 2:
            return 0
        l = 0
        count = nums[0] + 1
        res = 1

        while 1:
            if count >= len(nums):
                break
            for ii in range(l, count):
                if ii > len(nums) - 1:
                    break
                if ii == l:
                    maxx = count
                if nums[ii] + ii + 1 > maxx:
                    maxx = nums[ii] + ii + 1
                    index = ii

            if maxx > count:
                res += 1
                l = index
                count = maxx

        return res


print(Solution().jump([1, 2]))
print(Solution().jump([2,1]))
print(Solution().jump([2,3,1,1,4]))
print(Solution().jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))