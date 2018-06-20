# -*- coding: utf-8 -*-
# @StartTime : 2018/6/20 19:49
# @EndTime : 2018/6/20 19:49
# @Author  : Andy
# @Site    : 
# @File    : 58_length_of_last_word_180620.py
# @Software: PyCharm

"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = s.strip().split()
        if not ls:
            return 0
        return len(ls[-1])
