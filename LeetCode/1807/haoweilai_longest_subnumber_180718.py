# -*- coding: utf-8 -*-
# @StartTime : 2018/7/18 19:18
# @EndTime : 2018/7/18 19:24
# @Author  : Andy
# @Site    : 
# @File    : haoweilai_longest_subnumber_180718.py
# @Software: PyCharm

"""
题目描述
读入一个字符串str，输出字符串str中的连续最长的数字串
输入描述:
个测试输入包含1个测试用例，一个字符串str，长度不超过255。
输出描述:
在一行内输出str中里连续最长的数字串。
示例1
输入

abcd12345ed125ss123456789
输出

123456789
"""

class Solution(object):
    def longest(self, string):
        longest = ""
        size = len(string)
        temp = ""
        for char in string:
            if ord('0') <= ord(char) <= ord('9'):
                temp += char
            else:
                if len(temp) > len(longest):
                    longest = temp
                temp = ""
        if len(temp) > len(longest):
            longest = temp
        temp = ""
        return longest
input_val = raw_input()
print(Solution().longest(input_val))
print(Solution().longest("abcd12345ed125ss123456789"))
