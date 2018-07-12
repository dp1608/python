# -*- coding: utf-8 -*-
# @StartTime : 2018/7/12 20:25
# @EndTime : 2018/7/12 20:25
# @Author  : Andy
# @Site    : 
# @File    : 048_add_180712.py
# @Software: PyCharm

"""
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""


# -*- coding:utf-8 -*-
# class Solution:
#     def Add(self, num1, num2):
#         # write code here
#         sum = 0
#         while num2:
#             sum = num1 ^ num2
#             carry = (num1 & num2) << 1
#             num1 = sum
#             num2 = carry
#         return num1
# print(Solution().Add(-1, 2))
# print(bin(10))




# print("13231".pop())



import ctypes
class Solution:
    def Add(self, num1, num2):
        if num2 == 0:
            return num1
        return self.Add(num1 ^ num2, ctypes.c_int32((num1 & num2)).value << 1)
print(Solution().Add(-1, 2))