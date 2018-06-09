# -*- coding: utf-8 -*-
# @StartTime : 2018/6/9 21:28
# @EndTime : 2018/6/9 21:28
# @Author  : Andy
# @Site    : 
# @File    : 180609longest_common_prefix.py
# @Software: PyCharm


"""

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        size_str = len(strs)
        if size_str < 1:
            return ""
        res = ""
        count = 0
        min_size = len(strs[0])
        for str in strs:
            min_size = min(min_size, len(str))

        while count < min_size:
            temp = res + strs[0][count]
            for i in range(size_str):
                if temp != strs[i][0:count + 1]:
                    return res
            count += 1
            res = temp
        return res


s1 = ["flower","flow","flight"]
s1 = ["dog","doracecar","docar"]
print(Solution().longestCommonPrefix(s1))






