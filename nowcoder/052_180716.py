# -*- coding: utf-8 -*-
# @StartTime : 2018/7/16 10:04
# @EndTime : 2018/7/16 11:12
# @Author  : Andy
# @Site    : 
# @File    : 052_180716.py
# @Software: PyCharm

"""
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

"""


# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here

        def match_core(s, pattern):
            if not s and not pattern:
                return True
            elif not pattern:
                return False
            elif len(pattern) == 1 and len(s) == 1 and pattern[0] == s[0]:
                return match_core(s[1:], pattern[1:])

            elif len(pattern) > 1 and pattern[1] == '*':
                return match_core(s, pattern[2:]) \
                       or (len(s) >= 1 and (s[0] == pattern[0] or pattern[0] == '.') and match_core(s[1:], pattern[2:])) \
                       or (len(s) >= 1 and (s[0] == pattern[0] or pattern[0] == '.') and match_core(s[1:], pattern))
            elif s and pattern[0] != '.' and s[0] != pattern[0]:
                return False
            elif not s:
                return False
            else:
                return match_core(s[1:], pattern[1:])
        return match_core(s, pattern)


print(Solution().match("ab",".*a*a"))
# print(Solution().match("a", "ab*a"))
# print(Solution().match("aaa", "ab*ac*a"))
# print(Solution().match("a", ".*"))
# print(Solution().match("", "."))
# print "123"[4:]

