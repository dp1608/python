# -*- coding: utf-8 -*-
# @StartTime : 2018/6/25 20:41
# @EndTime : 2018/6/25 21:18
# @Author  : Andy
# @Site    : 
# @File    : 79_word_search_180625.py
# @Software: PyCharm

"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        if len(board[0]) < 1:
            return False
        row = len(board)
        col = len(board[0])

        path = [[0 for _ in range(col)] for ii in range(row)]

        def dfs(word, board, path, row_now, col_now):
            if len(word) == 0:
                return True
            char = word[0]
            if row_now > 0 and path[row_now - 1][col_now] != 1 and board[row_now - 1][col_now] == char:
                path[row_now - 1][col_now] = 1
                if dfs(word[1:], board, path, row_now - 1, col_now):
                    return True
                path[row_now - 1][col_now] = 0
            if row_now < len(path) - 1 and path[row_now + 1][col_now] != 1 and board[row_now + 1][col_now] == char:
                path[row_now + 1][col_now] = 1
                if dfs(word[1:], board, path, row_now + 1, col_now):
                    return True
                path[row_now + 1][col_now] = 0
            if col_now > 0 and path[row_now][col_now - 1] != 1 and board[row_now][col_now - 1] == char:
                path[row_now][col_now - 1] = 1
                if dfs(word[1:], board, path, row_now, col_now - 1):
                    return True
                path[row_now][col_now - 1] = 0
            if col_now < len(path[0]) - 1 and path[row_now][col_now + 1] != 1 and board[row_now][col_now + 1] == char:
                path[row_now][col_now + 1] = 1
                if dfs(word[1:], board, path, row_now, col_now + 1):
                    return True
                path[row_now][col_now + 1] = 0

        char = word[0]
        for i in range(row):
            for j in range(col):
                if char == board[i][j]:
                    path[i][j] = 1
                    if dfs(word[1:], board, path, i, j):
                        return True
                    path[i][j] = 0
        return False


board = [   ['A','B','C','E'],   ['S','F','C','S'],   ['A','D','E','E'] ]
word = "ABCCED"
word = "SEE"
word = "ABCB"
word = "ABCCSEE"
board = [['a'], ['a']]
word = "aaa"

board = [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]]
word = "ABCESEEEFS"
print(Solution().exist(board, word))


