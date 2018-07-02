# -*- coding: utf-8 -*-
# @StartTime : 2018/5/13 21:17
# @EndTime : 2018/5/13 21:17
# @Author  : Andy
# @Site    : 
# @File    : 180513jump_game.py
# @Software: PyCharm
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

#
# class Solution(object):
#     def canJump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         size = len(nums)
#         count = 0
#         index = size - 1
#         while 1:
#             if index == 0:
#                 return True
#             for j in range(index - 1, -1, -1):
#                 if (nums[j] + j) >= index:
#                     index = j
#                     break
#                 if j == 0:
#                     count += 1
#             if count == size:
#                 return False


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        index = size - 1
        for i in range(index)[::-1]:
            if i + nums[i] >= index:
                index = i
        return not index



So = Solution()
print(So.canJump([2,0]))
print(So.canJump([2,3,1,1,4]))