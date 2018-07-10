# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/10 16:05
# @End_time: 2018/7/10 16:19
# @Author  : Andy
# @Site    : 
# @File    : 027_premutation_string_180710.py

"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,
则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
"""

# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        l = list(ss)
        l.sort()

        ss = "".join(l)
        res = []

        def dfs(ss, path):
            if not ss:
                res.append(path)
            for i in range(len(ss)):
                dfs(ss[0:i] + ss[i + 1:], path + [ss[i]])
        dfs(ss, [])
        res_s = []
        for i in res:
            temp = "".join(i)
            if temp not in res_s:
                res_s.append("".join(i))
        # print(res_s)
        return res_s


print Solution().Permutation("")