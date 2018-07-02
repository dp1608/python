# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/2 16:29
# @End_time: 2018/7/2 16:39
# @Author  : Andy
# @Site    : 
# @File    : 125_valid_palindrome_180702.py

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        sub_s = s.lower()
        sub_s2 = ""
        for char in sub_s:
            if ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9'):
                sub_s2 += char
        sub_s3 = sub_s2[::-1]
        if sub_s2 == sub_s3:
            return True
        else:
            return False


a = "A man, a plan, a canal: Panama"
print(a)
# print(Solution().isPalindrome(a))