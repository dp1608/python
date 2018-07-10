# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/10 14:30
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 034_first_not_repeating_char_180710.py

"""
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1.
"""


# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        count_char = [0 for _ in range(256)]
        for i in s:
            count_char[ord(i)] += 1
        for i in s:
            if count_char[ord(i)] == 1:
                return s.index(i)
        return -1


# 链接：https://www.nowcoder.com/questionTerminal/1c82e8cf713b4bbeb2a5b31cf5b0417c
# 来源：牛客网

# class Solution:
#     def FirstNotRepeatingChar(self, s):
#         # write code here
#         if len(s)<0:
#             return -1
#         for i in s:
#             if s.count(i)==1:
#                 return s.index(i)
#                 break
#         return -1