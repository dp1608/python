# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/27 17:16
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 93_restore_ip_addresses.py

"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        size = len(s)
        if size < 4 or size > 12:
            return []
        res = []

        def dfs(string, n, path):
            if n == 0:
                if not string:
                    res.append(".".join(path))
                    return
                else:
                    return
            if not string:
                return
            dfs(string[1:], n - 1, path + [string[0]])

            if len(string) > 1:
                temp1 = string[0:2]
                if '10' <= temp1 <= '99':
                    dfs(string[2:], n - 1, path + [string[0:2]])
            if len(string) > 2:
                temp2 = string[0:3]
                if '100' <= temp2 < '256':
                    dfs(string[3:], n - 1, path+[string[0:3]])

        dfs(s, 4, [])

        return res

# s = "25525511135"
s = "010010"
print(Solution().restoreIpAddresses(s))
