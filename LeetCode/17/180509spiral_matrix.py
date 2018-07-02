# -*- coding: utf-8 -*-
# @StartTime : 2018/5/9 10:10
# @EndTime : 2018/5/9 10:10
# @Author  : Andy
# @Site    : 
# @File    : 180509spiral_matrix.py
# @Software: PyCharm


"""

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        size = m * n
        if size == 0:
            return []
        res.append(matrix[0][0])

        def wander(i, j, k):
            if len(res) == size:
                return
            direct = int(k / 4)
            if k % 4 == 1:
                for p in range(j + 1, n - direct):
                    res.append(matrix[i][p])
                k = k + 1
                # wander(i, n - 1 - direct, k)
                wander(i, n - direct - 1, k)
                return
            if k % 4 == 2:
                for p in range(i + 1, m - direct):
                    res.append(matrix[p][j])
                k = k + 1
                # wander(n - 1 - direct, j)
                wander(p, j, k)
                return
            if k % 4 == 3:
                for p in range(j - 1, direct - 1, -1):
                    res.append(matrix[i][p])
                k = k + 1
                wander(i, p, k)
                return
            if k % 4 == 0:
                for p in range(i - 1, direct - 1, -1):
                    res.append(matrix[p][j])
                k = k + 1
                wander(p, j ,k)
                return

        wander(0,0,1)
        return res

print(Solution().spiralOrder([[]]))
print(Solution().spiralOrder([[3],[2]]))
print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))