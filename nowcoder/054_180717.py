# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/17 14:54
# @End_time: 2018/7/17 16:13
# @Author  : Andy
# @Site    : 
# @File    : 054_180717.py

"""
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，
第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
"""

# -*- coding:utf-8 -*-
from collections import defaultdict
class Solution:

    def __init__(self):
        self.stream = ""

    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        dicts = defaultdict(int)
        for char in self.stream:
            dicts[char] += 1
        for char in self.stream:
            if dicts[char] == 1:
                return char
        return '#'
    def Insert(self, char):
        # write code here
        self.stream = self.stream + char

a = Solution()
print(a.Insert('g'))
print(a.FirstAppearingOnce())