# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/25 17:19
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 77_combinations_180625.py

"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        list = [_ + 1 for _ in range(n)]
        res = []
        print(list)
        def dfs(list, path, k):
            if k == 0:
                res.append(path)
                return
            if k < 0:
                return
            if not list:
                return
            size = len(list)

            for i in range(size):
                dfs(list[i + 1:], path + [list[i]], k - 1)

        dfs(list,[], k)
        return res
# print([1,23] + [3])

print(Solution().combine(4, 2))