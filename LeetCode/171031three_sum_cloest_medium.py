# -*- coding: utf-8 -*-
# @StartTime : 10/31/2017 10:01
# @EndTime   : 10/31/2017 10:43
# @Author    : Andy
# @Site      : 
# @File      : 171031three_sum_cloest_medium.py
# @Software  : PyCharm

"""
Given an array S of n integers, find three integers in S such that the sum is
closest to a given number, target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        sum = nums[0] + nums[1] + nums[2]
        most_closest =  sum
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            sum = nums[i] + nums[l] + nums[r]
            ll = 0
            # rr = 0
            most_closest = sum if abs(sum - target) < abs(most_closest - target) \
                else most_closest
            while sum - target < 0 and l < r - 1:
                l += 1
                sum = nums[i] + nums[l] + nums[r]
                most_closest = sum if abs(sum - target) < abs(most_closest - target) \
                    else most_closest
            while sum - target > 0 and r > l + 1:
                r -= 1
                sum = nums[i] + nums[l] + nums[r]
                most_closest = sum if abs(sum - target) < abs(most_closest - target) \
                    else most_closest
            while sum - target < 0 and l < r - 1:
                l += 1
                sum = nums[i] + nums[l] + nums[r]
                most_closest = sum if abs(sum - target) < abs(most_closest - target) \
                    else most_closest
                while sum - target > 0 and r > l + 1:
                    r -= 1
                    sum = nums[i] + nums[l] + nums[r]
                    most_closest = sum if abs(sum - target) < abs(
                        most_closest - target) \
                        else most_closest
        return most_closest

So = Solution()
print So.threeSumClosest([1, 1, 1, 2], 4)
print So.threeSumClosest([0, 1, 2], 0)
print So.threeSumClosest([0,-4,1,-5], 0)
print So.threeSumClosest([1,2,4,8,16,32,64,128],82)
print So.threeSumClosest([-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33],0)


