# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/12 12:07
# @End_time: 2018/6/12 14:19
# @Author  : Andy
# @Site    : 
# @File    : 180612generate_parenteses.py

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left = right = n
        res = []

        def generate_main(left, right, n, str):
            if left > right:
                return
            if left < 0:
                return
            if right < 0:
                return
            if len(str) == 2 * n:
                res.append(str)
                return
            generate_main(left - 1, right, n, str + '(')
            generate_main(left, right - 1, n, str + ')')
        generate_main(left, right, n, "")
        return res

print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(2))