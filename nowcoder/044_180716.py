# -*- coding: utf-8 -*-
# @StartTime : 2018/7/16 16:43
# @EndTime : 2018/7/16 16:52
# @Author  : Andy
# @Site    : 
# @File    : 044_180716.py
# @Software: PyCharm

"""
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，
有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。
后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
"""


# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return ""
        res = s.split()
        if not res:
            return s
        res = res[::-1]
        return " ".join(res)
print(Solution().ReverseSentence("student. a am I"))