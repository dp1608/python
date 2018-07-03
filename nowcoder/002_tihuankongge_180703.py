# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/3 15:20
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 002_tihuankongge_180703.py

"""
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


# -*- coding:utf-8 -*-
class Solution(object):
    # s 源字符串
    def replaceSpace(self, s):
        res = []
        for i in range(len(s)):
            if s[i] == ' ':
                res.append(i)
        for i in range(len(res)):
            index = res[i] + 2 * i
            s = s[:index] + "%20" + s[index + 1:]
        # s.replace(' ', "%20")
        return s

print(Solution().replaceSpace("  we are happy  "))
print(Solution().replaceSpace("   "))

