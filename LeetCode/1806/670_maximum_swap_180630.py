# -*- coding: utf-8 -*-
# @StartTime : 2018/6/30 9:54
# @EndTime : 2018/6/30 9:54
# @Author  : Andy
# @Site    : 
# @File    : 670_maximum_swap_180630.py
# @Software: PyCharm

"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
"""


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num_pre = str(num)

        maximum = num
        str_num = list(str_num_pre[:])
        for i in range(len(str_num)):
            for j in range(len(str_num)):
                temp = str_num[i]
                str_num[i] = str_num[j]
                str_num[j] = temp
                if int("".join(str_num)) > maximum:
                    maximum = int("".join(str_num))
                str_num =list(str_num_pre[:])

        return maximum

print(Solution().maximumSwap(2736))