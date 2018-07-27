# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/27 9:18
# @End_time: 2018/7/27 10:22
# @Author  : Andy
# @Site    : 
# @File    : 139_word_break_180727.py


"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s
can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

#
# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """
#         if not wordDict:
#             return False
#         word_set = set(wordDict)
#
#         def core(s):
#             if not s:
#                 return True
#             if s in word_set:
#                 return True
#             for i in range(len(s)):
#                 if s[0:i + 1] in word_set:
#                     if core(s[i + 1:]):
#                         return True
#             return False
#         res = core(s)
#         return res




class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict:
            return False
        size = len(s)
        dp = [False for _ in range(size + 1)]
        dp[0] = True
        for i in range(1, size + 1, 1):
            for word in wordDict:
                if dp[i - len(word)] and word == s[i - len(word): i ]:
                    dp[i] = True

        return dp[-1]


words = ["leet", "code"]
s = "leetcode"

# s = "goalspecial"
# words = ["go", "goal", "goals", "special"]
print(Solution().wordBreak(s, words))