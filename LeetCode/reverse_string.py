# -*- coding: utf-8 -*-
# @StartTime : 9/27/2017 20:40
# @EndTime   : 9/27/2017 20:40
# @Author    : Andy
# @Site      : 
# @File      : reverse_string.py
# @Software  : PyCharm

"""
    Write a function that takes a string as input and returns the string reversed.
    Example:
    Given s = "hello", return "olleh".
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return_str=s[::-1]
        return return_str