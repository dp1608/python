# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/3 11:49
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 130_surrounded_regions_180703.py

"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to
'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        row = len(board)
        col = len(board[0])

        def is_boundary(board):
            for j in range(col):
                if board[0][j] == 'O':
                    board[0][j] = 'S'
                if board[row - 1][j] == 'O':
                    board[row - 1][j] = 'S'
            for i in range(row):
                if board[i][0] == 'O':
                    board[i][0] = 'S'
                if board[i][col - 1] == 'O':
                    board[i][col - 1] = 'S'

        def expand_s(i, j):
            # visited.add(row_col2_one(i,j))
            if i < 0 or j < 0 or i >= row or j >= col:
                return
            if board[i][j] == 'O':
                board[i][j] = 'S'
                expand_s(i - 1, j)
                expand_s(i + 1, j)
                expand_s(i, j + 1)
                expand_s(i, j - 1)
            return

        is_boundary(board)
        for j in range(col):
            if board[0][j] == 'S':
                expand_s(1, j)
            if board[row - 1][j] == 'S':
                expand_s(row - 2, j)
        for i in range(row):
            if board[i][0] == 'S':
                expand_s(i, 1)
            if board[i][col - 1] == 'S':
                expand_s(i, col - 2)

        # print(board)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'
                else:
                    continue
        # print(board)

#
# board = [
# ['X', 'X', 'X', 'X'],
# ['X', 'O', 'O', 'X'],
# ['X', 'X', 'O', 'X'],
# ['X', 'O', 'X', 'X'],
# ]
board =[["O","O","O"],["O","O","O"],["O","O","O"]]
Solution().solve(board)