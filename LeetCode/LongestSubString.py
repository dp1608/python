# -*- coding: utf-8 -*-
# @StartTime : 2017/4/8 22:25
# @EndTime   : 2017/7/18 9:43
# @Author    : Andy
# @File      : LongestSubString.py
# @Software  : PyCharm

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=maxLength=0
        usedchar={}
        # l=min(26,len(s))
        for i in range(len(s)):             #consider there is always lower case
            if s[i] in usedchar and start<=usedchar[s[i]]:
                start=usedchar[s[i]]+1
            else:
                maxLength=max(maxLength,i-start+1)

            usedchar[s[i]]=i

        return maxLength




