# -*- coding: utf-8 -*-
# @StartTime : 2018/5/9 9:14
# @EndTime : 2018/5/9 10:00
# @Author  : Andy
# @Site    : 
# @File    : 180509rotate_image.py
# @Software: PyCharm

"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
 DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix_size = len(matrix)
        n = matrix_size
        if matrix_size % 2 == 1:
            loop1 = matrix_size // 2 + 1
            loop2 = loop1 - 1
        else:
            loop1 = matrix_size // 2
            loop2 = loop1
        for i in range(loop1):
            for j in range(loop2):
                a = matrix[i][j]
                b = matrix[j][n - 1 - i]
                c = matrix[n - 1 - i][n - 1 - j]
                d = matrix[n - 1 - j][i]
                matrix[i][j] = d
                matrix[j][n - 1 - i] = a
                matrix[n - 1 - i][n - 1 - j] = b
                matrix[n - 1 - j][i] = c
        return


# matrix =[
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(matrix)
print(matrix)
