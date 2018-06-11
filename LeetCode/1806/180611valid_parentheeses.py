# -*- coding: utf-8 -*-
# @StartTime : 2018/6/11 21:29
# @EndTime : 2018/6/11 21:29
# @Author  : Andy
# @Site    : 
# @File    : 180611valid_parentheeses.py
# @Software: PyCharm

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        size = len(s)
        if size < 1:
            return True
        

