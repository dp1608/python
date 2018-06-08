# -*- coding: utf-8 -*-
# @StartTime : 2018/6/8 20:21
# @EndTime : 2018/6/8 20:21
# @Author  : Andy
# @Site    : 
# @File    : 180608string_to_integer(atoi).py
# @Software: PyCharm

"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace
character is found. Then, starting from this character, takes an optional initial plus or minus sign followed
by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and
have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence
exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1)
or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        size = len(str)
        positive = True
        res = 0
        index = 0
        while index < size and str[index] == ' ':
            index += 1
        if index < size and str[index] == '-':
            positive = False
            index += 1
        elif index < size and str[index] == '+':
            positive = True
            index += 1
        while index < size and ord(str[index]) <= ord('9') and  ord(str[index]) >= ord('0'):
            res = res * 10 + ord(str[index]) - ord('0')
            index += 1
        if positive:
            return min(res, 0x7fffffff)
        else:
            return max(-res, -0x80000000)


if __name__ == '__main__':
    s1 = '42'
    s1 = "   -42"
    s1 = "4193 with words"
    s1 = "words and 987"
    s1 = "91283472332"
    print(Solution().myAtoi(s1))