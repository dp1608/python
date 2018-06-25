# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/25 10:42
# @End_time:  2018/6/25 11:52
# @Author  : Andy
# @Site    : 
# @File    : 67_add_binary_180625.py

"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Input:
"100"
"110010"
Output:
"1010000"
Expected:
"110110"
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not len(a):
            return b
        if not len(b):
            return a

        def add_core(a, b):
            # for char in b:
            #     if char != '1' or char != '0':
            #         valid_input = False
            #         return 0
            valid_input = True
            c = [0 for _ in range(len(a) + 1)]
            index_c = len(a)
            for i in range(len(b) - 1, -1, -1):
                ii = i + len(a) - len(b)
                if a[ii] != '1' and a[ii] != '0' or b[i] != '1' and b[i] != '0':
                    valid_input = False
                    return 0
                temp = int(a[ii]) + int(b[i]) + c[index_c]
                if temp > 1:
                    c[index_c] = temp - 2
                    c[index_c - 1] = 1
                else:
                    c[index_c] = temp
                index_c -= 1
            for j in range(len(a) - len(b) - 1, -1, -1):
                # jj = j + len(b)
                if a[j] != '1' and a[j] != '0':
                    valid_input = False
                    return 0
                temp = int(a[j]) + c[index_c]
                if temp > 1:
                    c[index_c] = temp - 2
                    c[index_c - 1] = 1
                else:
                    c[index_c] = temp
                index_c -= 1

            return valid_input, c

        # make sure that a is the longer string
        if len(a) < len(b):
            valid_input, c = add_core(b, a)
        else:
            valid_input, c = add_core(a, b)

        if not valid_input:
            return
        # return c
        return str(int("".join(map(str, c))))

print(Solution().addBinary("1010", "1011"))
print(Solution().addBinary("100", "110010"))


