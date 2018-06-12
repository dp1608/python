# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/12 16:13
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 180612implement_strstr.py

"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().

"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        size = len(needle)
        for i in range(len(haystack)):
            # j = 0
            if haystack[i:size + i] == needle[0:size]:
                return i
            # while j < size:
            #     if haystack
        return -1

print(Solution().strStr("hello","ll"))
# print("hello"[2:4])
