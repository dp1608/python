# -*- coding: utf-8 -*-
# @StartTime : 2018/8/24 10:18
# @EndTime : 2018/8/24 10:18
# @Author  : Andy
# @Site    : 
# @File    : 32_longest_valid_parentheses.py
# @Software: PyCharm

"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed)
 parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        res.append(0)
        list_s = list(s)
        for i in range(1, len(list_s)):
            if list_s[i] == '(':
                res.append(0)
            elif res[-1] > 0:
                temp = res[-1]
                if i - temp - 1 >= 1 and list_s[i - temp - 1] == '(':
                    res.append(res[-1] + 2 + res[- temp - 2])
                elif i - temp - 1 >= 0 and list_s[i - temp - 1] == '(':
                    res.append(res[-1] + 2)
                else:
                    res.append(0)
            elif res[-1] == 0:
                if len(res) >= 2 and list_s[i - 1] == '(':
                    res.append(res[-2] + 2)
                elif list_s[i - 1] == '(':
                    res.append(2)
                else:
                    res.append(0)
        return max(res)

s = '(()'
# s = ")()())"
# s = '())'
# s = "()(())"
s = "))))((()(("
print(Solution().longestValidParentheses(s))