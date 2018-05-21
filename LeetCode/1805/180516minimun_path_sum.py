# -*- coding: utf-8 -*-
# @StartTime : 2018/5/16 19:43
# @EndTime : 2018/5/16 19:43
# @Author  : Andy
# @Site    : 
# @File    : 180516minimun_path_sum.py
# @Software: PyCharm


"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the
sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m < 1:
            return
        n = len(grid[0])
        for i in range(m - 2, -1, -1):
            grid[i][n - 1] = grid[i + 1][n - 1] + grid[i][n - 1]
        for j in range(n - 2, -1, -1):
            grid[m - 1][j] = grid[m - 1][j + 1] + grid[m - 1][j]
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                grid[i][j] = min(grid[i + 1][j], grid[i][j + 1]) + grid[i][j]
        return grid[0][0]


print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
