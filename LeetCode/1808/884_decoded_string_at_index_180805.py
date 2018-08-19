# -*- coding: utf-8 -*-
# @StartTime : 2018/8/5 10:06
# @EndTime : 2018/8/5 10:06
# @Author  : Andy
# @Site    : 
# @File    : 884_decoded_string_at_index_180805.py
# @Software: PyCharm


"""
An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is read one character
 at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.
Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.



Example 1:

Input: S = "leet2code3", K = 10
Output: "o"
Explanation:
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
Example 2:

Input: S = "ha22", K = 5
Output: "h"
Explanation:
The decoded string is "hahahaha".  The 5th letter is "h".
Example 3:

Input: S = "a2345678999999999999999", K = 1
Output: "a"
Explanation:
The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".
"""


# class Solution(object):
#     def decodeAtIndex(self, S, K):
#         """
#         :type S: str
#         :type K: int
#         :rtype: str
#         """
#         res = [S[0]]
#         index = 1
#         while len(res) < K:
#             char = S[index]
#             if ord('0') <= ord(char) <= ord('9'):
#                 count = int(char) - 1
#                 temp = res[:]
#                 while len(res) < K and count > 0:
#                     res += temp[:]
#                     count -= 1
#                 if len(res) >= K:
#                     break
#                 index += 1
#             else:
#                 res += char
#                 index += 1
#
#         return res[K - 1]


class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        len_res = 0
        count = 0

        for char in S:
            temp = len_res
            if ord('0') <= ord(char) <= ord('9'):
                len_res *= int(char)
                count += 1
                if len_res >= K:
                    return self.decodeAtIndex(S, K - temp)
            else:
                len_res += 1
                if len_res == K:
                    return char

print(Solution().decodeAtIndex("ha22", 5))