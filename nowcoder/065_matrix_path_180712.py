# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/12 11:41
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 065_matrix_path_180712.py

"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，
每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
 例如
 a b c e
 s f c s
 a d e e
 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
 但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""


# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not path:
            return True
        if not matrix:
            return False
        new_matrix = []
        for i in range(rows):
            temp = []
            for j in range(cols):
                temp.append(matrix[cols * i + j])
            new_matrix.append(temp)
        # print(new_matrix)
        # return

        def verify(res, arr, row, col, path):
            if not path:
                return True
            if row >= len(arr) or row < 0 or col < 0 or col >= len(arr[0]):
                return False
            if res[row][col] == 1:
                return False
            if arr[row][col] != path[0]:
                return False
            else:
                res[row][col] = 1
                return verify(res, arr, row + 1, col, path[1:]) or verify(res, arr, row - 1, col, path[1:]) \
                       or verify(res, arr, row, col + 1, path[1:]) or verify(res, arr, row, col - 1, path[1:])

        res = [[0 for _ in range(cols)] for _j in range(rows)]
        char = path[0]
        for i in range(rows):
            for j in range(cols):
                if char == new_matrix[i][j]:
                    # res[i][j] = 1
                    if verify(res, new_matrix, i, j, path[0:]):
                        return True
                    else:
                        res = [[0 for _ in range(cols)] for _j in range(rows)]
        return False


print Solution().hasPath("123412341234",3,4,"1234443222")
