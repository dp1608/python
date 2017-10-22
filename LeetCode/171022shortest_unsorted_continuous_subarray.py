# -*- coding: utf-8 -*-
# @StartTime : 10/22/2017 21:33
# @EndTime   : 10/22/2017 21:33
# @Author    : Andy
# @Site      : 
# @File      : 171022shortest_unsorted_continuous_subarray.py
# @Software  : PyCharm

"""
Given an integer array, you need to find one continuous subarray that if
you only sort this subarray in ascending order, then the whole array will
be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make
the whole array sorted in ascending order.

Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""

# AC is < 30%. But me is one time to AC
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        col = len(nums)
        # max_index = col - 1
        min_index = 10001
        count2 = 0
        count1 = 0
        for i in range(0, col - 1):
            if nums[i] > nums[i + 1]:
                min_index = min(min_index, i)
                max_index = i + 1
        if min_index != 10001:
            min_num = min(nums[min_index:max_index + 1])
        else:
            return 0
        max_num = max(nums[min_index:max_index + 1])
        for i in range(0, col):
            if min_num < nums[i]:
                count1 = i
                break
        for i in range(col - 1, -1, -1):
            if max_num > nums[i]:
                count2 = i
                break
        return count2 - count1 + 1

So = Solution()
print So.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])

print So.findUnsortedSubarray([0])