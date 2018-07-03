# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/3 14:16
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 131_palindrome_partitioning_180703.py

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
        res = []

        def is_pal(s):
            return s == s[::-1]

        def dfs(s, path):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s) + 1):
                if is_pal(s[:i]):
                    dfs(s[i:], path + [s[:i]])

        dfs(s, [])
        return res

a = [1,2,3,45,5,6,6]
print(a[:3])
