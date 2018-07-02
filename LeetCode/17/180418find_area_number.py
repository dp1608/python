# -*- coding: utf-8 -*-
# @StartTime : 18/4/2018 11:18
# @EndTime   : 18/4/2018 13:34
# @Author    : Andy
# @Site      :
# @File      : 180418find_area_number.py
# @Software  : PyCharm

import numpy as np
import math

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
Given the above grid, return 11. Note the answer is not 6, because the island must be connected 8-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
"""


class Solution(object):
    def count_area(self, grid):
        """
        count number of area
        :type grid: List[List[int]]
        :rtype: list area of every area
        """
        grid1 = np.array(grid)
        id_area = np.array(grid)
        area = []
        row = len(grid)
        col = len(grid[0])
        k = 1
        for i in range(row):
            for j in range(col):
                temp_area = self.find_area(grid1, i, j, k, id_area)
                if temp_area > 0:
                    k += 1
                    area.append(temp_area)
        return area, len(area), id_area

    def find_area(self, grid, row, col, k, id_area):
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
            id_area[row][col] = k
            result = self.find_area(grid, row - 1, col, k, id_area) + \
                     self.find_area(grid, row + 1, col, k, id_area) + \
                     self.find_area(grid, row, col + 1, k, id_area) + \
                     self.find_area(grid, row, col - 1, k, id_area) + \
                     self.find_area(grid, row - 1, col - 1, k, id_area) + \
                     self.find_area(grid, row + 1, col + 1, k, id_area) + \
                     self.find_area(grid, row - 1, col + 1, k, id_area) + \
                     self.find_area(grid, row + 1, col - 1, k, id_area) + 1
            return result

    def compute_distance(self, grid, x0, y0):
        """
        Output all min_distance of areas.
        When you run this function, id_area is already computed, which means function count_area is ran.
        :param grid:
        :param row: x0
        :param col: y0
        :return: list: all min_distance of areas
        """
        distance = [9999.0 for p in range(count)]
        # every traversal compute the min_distance of one area
        # for k in range(1, count + 1, 1):
        #     min_disatance = 9999
        #     if self.in_area_k(grid, row, col, k):
        #         min_disatance = 0
        #         distance.append(min_disatance)
        #     else:
        #
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if id_area[i][j] != 0:
                    k = id_area[i][j]
                    temp_distance = self.compute_distance_in(x0, y0, i, j)
                    distance[k - 1] = min(distance[k - 1], temp_distance)
        return distance

    def compute_distance_in(self, x0, y0, i, j):
        return math.sqrt((x0 - i) * (x0 - i) + (y0 - j) * (y0 - j))

    def del_area(self, grid1, area, min_area, id_area):
        grid_then = np.array(grid1)
        temp = []
        for k in range(len(area)):
            if area[k] <= min_area:
                temp.append(k + 1)

        row = len(grid1)
        col = len(grid1[0])
        for i in range(row):
            for j in range(col):
                if id_area[i][j] in temp:
                    grid_then[i][j] = 0
        return grid_then




    # def in_area_k(self, x0, y0, k):
    #     if id_area[x0][y0] == k:
    #         return True
    #     else:
    #         return False


Max = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

# id_area = np.array(grid)
# x0 y0 is Image Coordinate System 0,6 means first row, seventh col
x0 = 0
y0 = 6


area_of_area, count, id_area = Max.count_area(grid)

distance2 = Max.compute_distance(grid, x0, y0)
grid1 = Max.del_area(grid, area_of_area, 2, id_area)

# count = len(result)
print('finish')
# print(result)
# print(count)
# print(grid)
# print(grid1)
print("every area's area", area_of_area)
print("ID area:", id_area)
print("distance:", distance2)
print("del then grid is ", grid1)
print(id_area[0][2])