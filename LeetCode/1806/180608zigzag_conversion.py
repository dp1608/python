# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/8 17:43
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 180608zigzag_conversion.py

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        size = len(s)

        cvt_s = [[] for _ in range(numRows)]
        ss = ''
        traverse = 0
        positive = 1
        for i in range(size):
            cvt_s[traverse].append(s[i])
            if traverse == numRows - 1:
                positive = -1
            if traverse == 0:
                positive = 1
            traverse += positive

        for i in range(numRows):
            ss = ss + ''.join(cvt_s[i])
        return ss


s = "PAYPALISHIRING"
print(Solution().convert(s, 3))
# ss = Solution().convert(s, 3)
# ss = ''.join(cvt_s[0])
# print(ss)