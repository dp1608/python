# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/27 14:13
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 91_decode_ways_180627.py

"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        def valid_input(s):
            if not s:
                return False
            if s[0] == '0':
                return False
            for i in range(len(s)):
                char = s[i]
                if ord(char) > ord('9') or ord(char) < ord('0'):
                    return False
                if char == '0' and ((s[i - 1] != '1') and (s[i - 1] != '2')):
                    return False
            return True

        if not valid_input(s):
            return 0

        i = 0
        while i < len(s):
            if s[i] == '0':
                s = s[0:i - 1] + s[i + 1:]
            i += 1

        size = len(s)
        res = [1]

        j = size - 1
        while j >= 0:
            if j < size - 2:
                two_sum = int(s[j:j + 2])
                if 27 > int(two_sum) > 10:
                    res.append(res[-1] + res[-2])
                else:
                    res.append(res[-1])
            elif j == size - 1:
                j -= 1
                continue
            else:
                two_sum = int(s[j:j + 2])
                if 27 > int(two_sum) > 10:
                    res.append(2)
                else:
                    res.append(1)
            j -= 1
        return res[-1]

    def numDecodings2(self, s):
        if s == "":
            return 0
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":  #"01"ways = 0
                dp[i] += dp[i-2]
        return dp[len(s)]



# print(Solution().numDecodings("12120"))  # 3
print(Solution().numDecodings("1212"))  # 5  (1,2,1,2) (12, 12) (1, 21, 2) (12, 1, 2) (1,2,12)
print(Solution().numDecodings("110"))  # 1
print(Solution().numDecodings("101"))  # 1
print(Solution().numDecodings("10"))   # 1
print(Solution().numDecodings("11"))   # 2
print(Solution().numDecodings2("111"))  # 3
print(Solution().numDecodings2("2230"))  # 0
print(Solution().numDecodings(""))     # 0
# print(Solution().numDecodings("1"))    # 1
print(Solution().numDecodings2("0"))    # 0
print(Solution().numDecodings2("30"))   # 0


# def dynamic(s, now):
#     if s[-1] == '0':
#         if len(s) > 3:
#             return dynamic(s[0:-2], now)
#         else:
#             return now
#     if len(s) == 0:
#         return now
#     if len(s) == 1:
#         return now
#     two_sum = s[-2:]
#     if 27 > int(two_sum) > 10:
#         return dynamic(s[0:-1], now + 1)
#     else:
#         return dynamic(s[0:-1], now)
#
# return dynamic(s, 1)

# size = len(s)
# res = []
# 存在问题，110， 101的问题
# for i in range(size - 1, -1, -1):
#     if len(res) < 1:
#         res.append(1)
#         continue
#
#     if s[i] == '0':
#         if res and i > 1:
#             res[-1] -= 1
#         continue
#
#     count = res[-1]
#     two_num = s[i:i + 2]
#     if 27 > int(two_num) > 0 and int(two_num) != 10 and int(two_num) != 20:
#         count += 1
#         res.append(count)
#     else:
#         res.append(count)
#
# if not res:
#     return 0
# return res[-1]