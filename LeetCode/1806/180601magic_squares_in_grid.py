# -*- coding: utf-8 -*-
# @StartTime : 2018/6/1 14:04
# @EndTime : 2018/6/1 14:04
# @Author  : Andy
# @Site    : 
# @File    : 180601magic_squares_in_grid.py
# @Software: PyCharm

"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column,
and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).



Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
"""


class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        if row < 3:
            return 0
        col = len(grid[0])
        if col < 3:
            return 0
        count = 0

        def is_magic(grid, i, j):
            a1 = grid[i][j]
            a2 = grid[i][j+1]
            a3 = grid[i][j+2]
            a4 = grid[i+1][j]
            a5 = grid[i+1][j+1]
            a6 = grid[i+1][j+2]
            a7 = grid[i+2][j]
            a8 = grid[i+2][j+1]
            a9 = grid[i+2][j+2]
            sum = a1 + a2 + a3
            if a4 + a5 + a6 != sum:
                return False
            if a7 + a8 + a9 != sum:
                return False
            if a1 + a4 + a7 != sum:
                return False
            if (a2 + a5 + a8) != sum:
                return False
            if a1 + a5 + a9 != sum:
                return False
            if a3 + a5 + a7 != sum:
                return False
            return True

        for i in range(row - 2):
            for j in range(col - 2):
                if is_magic(grid, i, j):
                    count += 1

        return count


a = [[4,3,8,4], [9,5,1,9], [2,7,6,2]]
a = [[10,3,5],[1,6,11],[7,9,2]]
print(Solution().numMagicSquaresInside(a))

