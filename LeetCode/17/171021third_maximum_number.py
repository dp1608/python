# -*- coding: utf-8 -*-
# @StartTime : 10/21/2017 14:34
# @EndTime   : 10/21/2017 14:49
# @Author    : Andy
# @Site      : 
# @File      : 171021third_maximum_number.py
# @Software  : PyCharm

"""
Given a non-empty array of integers, return the third maximum number in this
array. If it does not exist, return the maximum number.
The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum
(2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum
distinct number.
Both numbers with value 2 are both considered as second maximum.
"""

#初始化花费了大量的代码行数，不过一遍AC哦
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_number = nums[0]
        for num in nums:
            if num > max_number:
                max_number = num

        if len(nums) < 3:
            return max_number

        # 初始化第二大的元素
        i = 0
        max_number2 = nums[i]
        while max_number2 == max_number:
            i += 1
            if i == len(nums):
                return max_number
            max_number2 = nums[i]


        for num in nums:
            if num > max_number2 and num < max_number:
                max_number2 = num

        # 初始化第三大的元素
        i = 0
        max_number3 = nums[i]
        while max_number3 == max_number or max_number3 == max_number2:
            i += 1
            if i == len(nums):
                return max_number
            max_number3 = nums[i]

        for num in nums:
            if num > max_number3 and num < max_number2:
                max_number3 = num

        if max_number3 == max_number or max_number3 ==max_number2:
            return max_number
        return max_number3

So = Solution()
print So.thirdMax([3, 2, 1])
print So.thirdMax([1, 2])