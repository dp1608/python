# -*- coding: utf-8 -*-
# @StartTime : 2018/6/9 12:35
# @EndTime : 2018/6/9 12:35
# @Author  : Andy
# @Site    : 
# @File    : 180609integer_to_roman.py
# @Software: PyCharm

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ""
        minus = num
        while minus >= 1000:
            minus -= 1000
            s += "M"
        while minus >= 900:
            minus -= 900
            s += "CM"
        while minus >= 500:
            minus -= 500
            s += "D"
        while minus >= 400:
            minus -= 400
            s += "CD"
        while minus >= 100:
            minus -= 100
            s += "C"
        while minus >= 90:
            minus -= 90
            s += "XC"
        while minus >= 50:
            minus -= 50
            s += "L"
        while minus >= 40:
            minus -= 40
            s += "XL"
        while minus >= 10:
            minus -= 10
            s += "X"
        while minus >= 9:
            minus -= 9
            s += "IX"
        while minus >= 5:
            minus -= 5
            s += "V"
        while minus >= 4:
            minus -= 4
            s += "IV"
        while minus >= 1:
            minus -= 1
            s += "I"
        return s


num = 3
num = 4
num = 9
num = 10
num = 58
num = 1994
print(Solution().intToRoman(num))