# -*- coding: utf-8 -*-
# @StartTime : 2018/5/16 9:21
# @EndTime : 2018/5/16 9:21
# @Author  : Andy
# @Site    :
# @File    : 180516spiral_matrix_II.py
# @Software: PyCharm

"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        A, lo = [], n * n + 1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [range(lo, hi)] + zip(*A[::-1])
        return map(list, A)


# print(Solution().generateMatrix(3))
