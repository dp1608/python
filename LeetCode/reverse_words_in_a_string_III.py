# -*- coding: utf-8 -*-
# @StartTime : 9/21/2017 22:00
# @EndTime   :
# @Author    : Andy
# @Site      : 
# @File      : reverse_words_in_a_string_III.py
# @Software  : PyCharm

"""
Given a string, you need to reverse the order of characters in each word wit
    hin a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will
    not be any extra space in the string.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        words = ''
        while i < len(s):
            temp = ''
            revers = ''
            while i < len(s) and s[i] != ' ':
                temp += s[i]
                i += 1

            for j in range(len(temp)-1,-1,-1):
                revers = revers[:len(temp)-j-1] + temp[j]+' '
            words = words + revers
            i += 1

            # print words
        words = words[:len(s)]
        return words


a=Solution()
print a.reverseWords("Let's take LeetCode contest")


