# -*- coding: utf-8 -*-
# @StartTime : 2018/8/5 9:35
# @EndTime : 2018/8/5 9:35
# @Author  : Andy
# @Site    : 
# @File    : 887_projection_180805.py
# @Software: PyCharm


class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        if not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])

        def xy(grid):
            temp = 0
            for i in range(row):
                for j in range(col):
                    if grid[i][j] != 0:
                        temp += 1
            return temp

        def xz(grid):
            temp = [0 for _ in range(row)]
            for i in range(row):
                temp[i] = max(grid[i])
            return sum(temp)

        def yz(grid):
            temp = [0 for _ in range(col)]
            for j in range(col):
                for i in range(row):
                    temp[j] = max(temp[j], grid[i][j])
            return sum(temp)

        return xy(grid) + yz(grid) + xz(grid)

grid = [[1,2],[3,4]]
print(Solution().projectionArea(grid))

