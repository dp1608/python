# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/17 14:12
# @End_time:  2018/7/17 14:51
# @Author  : Andy
# @Site    : 
# @File    : 053_180717.py

"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""


# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here

        def is_int(s):
            if len(s) < 1:
                return False
            for char in s:
                if ord('0') <= ord(char) <= ord('9'):
                    continue
                else:
                    return False
            return True

        def is_fuhao_int(s):
            if not s:
                return False
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
            return is_int(s)

        def is_xiaoshu(s):
            if not s:
                return False
            if '.' in s:

                if s[0] == '+' or s[0] == '-':
                    s = s[1:]
                index = s.index('.')
                if (is_fuhao_int(s[:index]) or index == 0) and is_int(s[index + 1:]):
                    return True
                else:
                    return False
            else:
                if is_fuhao_int(s):
                    return True
                else:
                    return False

        if not s:
            return False
        if 'e' in s:
            index = s.index('e')
            if is_xiaoshu(s[:index]) and is_fuhao_int(s[index + 1:]):
                return True
            else:
                return False
        elif 'E' in s:
            index = s.index('E')
            if is_xiaoshu(s[:index]) and is_fuhao_int(s[index + 1:]):
                return True
            else:
                return False
        else:
            if is_xiaoshu(s):
                return True
            else:
                return False


print(Solution().isNumeric("+100"))
print(Solution().isNumeric("5e2"))
print(Solution().isNumeric("-123"))
print(Solution().isNumeric("3.1416"))
print(Solution().isNumeric("-1E-16"))
print(Solution().isNumeric("-.123"))

print("----------")
print(Solution().isNumeric(""))
print(Solution().isNumeric("12e"))
print(Solution().isNumeric("3.+1416"))
print(Solution().isNumeric("1a3.14"))
print(Solution().isNumeric("1.2.3"))
print(Solution().isNumeric("+-5"))
print(Solution().isNumeric("12e4.3"))