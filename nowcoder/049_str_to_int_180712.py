# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/12 16:31
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 049_str_to_int_180712.py

"""
题目描述
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0
"""

# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0

        def verify(s):
            if not s:
                return False
            veri = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            for char in s:
                if char not in veri:
                    return False
            return True

        positive = True
        if s[0] == '+':
            s = s[1:]
            if not verify(s):
                return 0
        elif s[0] == '-':
            positive = False
            s = s[1:]
            if not verify(s):
                return 0
        else:
            if not verify(s):
                return 0
        res = 0
        for char in s:
            res = res * 10 + (ord(char) - ord('0'))
        if positive:
            return res
        else:
            return -res

print(Solution().StrToInt("1a33"))
#
# veri = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# for char in "1a33":
#     if char not in veri:
#         print(char)

