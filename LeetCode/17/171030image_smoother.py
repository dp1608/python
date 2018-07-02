# -*- coding: utf-8 -*-
# @StartTime : 10/30/2017 10:01
# @EndTime   : 10/30/2017 10:26
# @Author    : Andy
# @Site      : 
# @File      : 171030image_smoother.py
# @Software  : PyCharm


"""
Given a 2D integer matrix M representing the gray scale of an image, you need
to design a smoother to make the gray scale of each cell becomes the average
 gray scale (rounding down) of all the 8 surrounding cells and itself.
 If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].

"""


class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def exist(self,i,j):
            if i < roww  and i >= 0 and j < coll and j >= 0:
                return True
            else:
                return False

        roww = len(M)
        coll = len(M[0])
        N = [[None for i in range(coll)] for j in range(roww)]
        for row in range(roww):
            for col in range(coll):
                count = 0
                round_all = 0
                for i in range(row - 1,row + 2):
                    for j in range(col - 1,col + 2):
                        if exist(self,i,j):
                            count += 1
                            round_all += M[i][j]
                N[row][col] = int((round_all ) / float(count))
        return N




So = Solution()
print So.imageSmoother([[1,1,1], [1,0,1], [1,1,1]])
print So.imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]])





