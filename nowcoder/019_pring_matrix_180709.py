# -*- coding: utf-8 -*-
# @StartTime : 2018/7/9 21:37
# @EndTime : 2018/7/9 21:37
# @Author  : Andy
# @Site    : 
# @File    : 019_print_matrix_180709.py
# @Software: PyCharm

"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
则依次打印出数字
1,2,3,4,
8,12,16,15,
14,13,9,5,
6,7,11,10.
"""


# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix or not matrix[0]:
            return

        start = 0
        res = []
        row = len(matrix)
        col = len(matrix[0])

        def print_in_circle(start):
            end_y = row - 1 - start
            end_x = col - 1 - start

            for i in range(start, end_x + 1, 1):
                res.append(matrix[start][i])
            if start < end_y:
                for i in range(start + 1, end_y + 1, 1):
                    res.append(matrix[i][end_x])
            if start < end_x and start < end_y:
                for i in range(end_x - 1, start - 1, -1):
                    res.append(matrix[end_y][i])
            if start < end_x and start < end_y - 1:
                for i in range(end_y - 1, start, -1):
                    res.append(matrix[i][start])
        while col > start * 2 and row > start * 2:
            print_in_circle(start)
            start += 1
        return res
