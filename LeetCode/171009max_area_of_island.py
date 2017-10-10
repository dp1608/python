# -*- coding: utf-8 -*-
# @StartTime : 10/9/2017 14:18
# @EndTime   : 10/9/2017 15:15
# @Author    : Andy
# @Site      : 
# @File      : 171009max_area_of_island.py
# @Software  : PyCharm

"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water. Find the
maximum area of an island in the given 2D array. (If there is no island,
the maximum area is 0.)
Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                temp_area = self.findArea(grid,i,j)
                if temp_area > max_area:
                    max_area = temp_area
        return max_area


    def findArea(self,grid,row,col):
        if row < 0 or col < 0:
            return 0
        if row > len(grid)-1:
            return 0
        if col > len(grid[0])-1:
            return 0
        if grid[row][col] == 0:
            return 0
        elif grid[row][col] == 1:
            grid[row][col] = 0
            result = self.findArea(grid,row-1,col)+self.findArea(grid,row+1,col)+\
                   self.findArea(grid,row,col+1)+self.findArea(grid,row,col-1)+1
            return result

Max = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
result = Max.maxAreaOfIsland(grid)
print 'finish'
print result