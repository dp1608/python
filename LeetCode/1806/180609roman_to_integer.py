# -*- coding: utf-8 -*-
# @StartTime : 2018/6/9 13:38
# @EndTime : 2018/6/9 13:38
# @Author  : Andy
# @Site    : 
# @File    : 180609roman_to_integer.py
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
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        num = 0
        index = 0
        while index < size and s[index] == 'M':
            num += 1000
            index += 1
        while index < size - 1 and s[index] == 'C' and s[index + 1] == 'M':
            num += 900
            index += 2
        while index < size and s[index] == 'D':
            num += 500
            index += 1
        while index < size - 1 and s[index] == 'C' and s[index + 1] == 'D':
            num += 400
            index += 2

        while index < size and s[index] == 'C':
            num += 100
            index += 1
        while index < size - 1 and s[index] == 'X' and s[index + 1] == 'C':
            num += 90
            index += 2
        while index < size and s[index] == 'L':
            num += 50
            index += 1
        while index < size - 1 and s[index] == 'X' and s[index + 1] == 'L':
            num += 40
            index += 2

        while index < size and s[index] == 'X':
            num += 10
            index += 1
        while index < size - 1 and s[index] == 'I' and s[index + 1] == 'X':
            num += 9
            index += 2
        while index < size and s[index] == 'V':
            num += 5
            index += 1
        while index < size - 1 and s[index] == 'I' and s[index + 1] == 'V':
            num += 4
            index += 2

        while index < size and  s[index] == 'I':
            num += 1
            index += 1
        return num

s1 = "III"
s1 = "IX"
s1 = "LVIII"
s1 = "MCMXCIV"
print(Solution().romanToInt(s1))
