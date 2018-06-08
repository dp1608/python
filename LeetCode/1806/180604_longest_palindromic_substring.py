"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size == 1:
            return s
        if size == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        i = 0
        max_s = 1
        res = s[0]

        while i < size:
            j = i + 1
            while j < size:
                if s[j] == s[i]:
                    j += 1
                else:
                    break

            k = 0
            while i - k - 1 >=0 and j + k < size:
                if s[i - k - 1] == s[j + k]:
                    k += 1
                else:
                    break
            temp = j - i + 2 * k
            if temp > max_s:
                max_s = temp
                res = s[i - k:j + k]

            if j == size:
                break
            i = j
        return res


s = 'adbbdddddbda'
print(Solution().longestPalindrome(s))