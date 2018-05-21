# -*- coding: utf-8 -*-
# @StartTime : 2018/5/16 18:28
# @EndTime : 2018/5/16 18:28
# @Author  : Andy
# @Site    : 
# @File    : 180516unique_pathsII.py
# @Software: PyCharm

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        count_path = [[0 for _i in range(n)] for _j in range(m)]
        for j in range(n - 1, -1, -1):
            if obstacleGrid[m - 1][j] == 1:
                count_path[m - 1][j] = 0
                break
            else:
                count_path[m - 1][j] = 1

        for i in range(m - 1, -1, -1):
            if obstacleGrid[i][n - 1] == 1:
                count_path[i][n - 1] = 0
                break
            else:
                count_path[i][n - 1] = 1

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    count_path[i][j] = 0
                else:
                    count_path[i][j] = count_path[i + 1][j] + count_path[i][j + 1]
        return count_path[0][0]

A = [[0,0,0],[1,1,0],[0,0,0]]
# A = [[0,0]]
print(Solution().uniquePathsWithObstacles(A))
# print(A[0][1])




        #
        # def dy_count(i,j):
        #     if i < 0 or i > m -1 or j < 0 or j > m -1:
        #         return 0
        #     if obstacleGrid[i][j] == 1:
        #         return 0
        #     count_path[i][j] = dy_count(i-1)

