# -*- coding: utf-8 -*-
# @StartTime : 2018/5/16 17:00
# @EndTime : 2018/5/16 17:00
# @Author  : Andy
# @Site    : 
# @File    : 180516unique_paths.py
# @Software: PyCharm

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if min(m, n) < 1:
            return

        def combination(a,b):
            temp = 1
            for i in range(a, b, -1):
                temp = i * temp
            for j in range(1, a - b + 1):
                temp = temp / j
            return temp
        return combination(m + n - 2, n - 1)


print(Solution().uniquePaths(3,2))

