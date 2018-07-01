# -*- coding: utf-8 -*-
# @StartTime : 2018/7/1 10:03
# @EndTime : 2018/7/1 10:03
# @Author  : Andy
# @Site    : 
# @File    : 861.py
# @Software: PyCharm

"""
861. Score After Flipping Matrix My SubmissionsBack to Contest
User Accepted: 85
User Tried: 99
Total Accepted: 85
Total Submissions: 119
Difficulty: Medium
We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column:
changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number,
and the score of the matrix is the sum of these numbers.

Return the highest possible score.



Example 1:

Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39


Note:

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] is 0 or 1.
"""


class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        row = len(A)
        col = len(A[0])

        def inta(A):
            res = 0
            for i in range(len(A)):
                temp = 0
                for j in range(len(A[i])):
                    temp = temp << 1
                    temp += A[i][j]
                res += temp
            return res

        def shuiping(A,row):
            # B = A[:]
            for j in range(len(A[row])):
                A[row][j] = 1 - A[row][j]
            return A

        def chuizhi(A, col):
            for j in range(len(A)):
                A[j][col] = 1 - A[j][col]
            return A

        def count_A(A, col):
            res = 0
            for j in range(len(A)):
                if A[j][col] == 1:
                    res += 1
            return res


        for i in range(row):
            if A[i][0] != 1:
                A = shuiping(A,i)

        for j in range(1, col, 1):
            count_col = count_A(A, j)
            if count_col * 1.0 < row / 2.0:
                A = chuizhi(A, j)

        res = inta(A)
        return res

temp = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(Solution().matrixScore(temp))




