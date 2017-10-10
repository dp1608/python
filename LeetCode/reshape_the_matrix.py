# -*- coding: utf-8 -*-
# @StartTime : 9/28/2017 10:14
# @EndTime   : 9/28/2017 10:36
# @Author    : Andy
# @Site      : 
# @File      : reshape_the_matrix.py
# @Software  : PyCharm


"""
    In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into
a new one with different size but keep its original data. You're given a matrix represented
by a two-dimensional array, and two positive integers r and c
representing the row number and column number of the wanted reshaped matrix, respectively.
    The reshaped matrix need to be filled with all the elements
of the original matrix in the same row-traversing order as they were.
If the 'reshape' operation with given parameters is possible and legal, o
utput the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input:
    nums =
    [[1,2],
    [3,4]]
    r = 1, c = 4
Output:
    [[1,2,3,4]]
Explanation:
    The row-traversing of nums is [1,2,3,4]. The new reshaped
    matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input:
    nums =
    [[1,2],
     [3,4]]
    r = 2, c = 4
Output:
    [[1,2],
    [3,4]]
Explanation:
    There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
    The height and width of the given matrix is in range [1, 100].
    The given r and c are all positive.
"""


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        nums_row = len(nums)
        nums_col = len(nums[0])
        if r*c > nums_row*nums_col:
            return nums
        reshape_nums = [[0 for col in range(c)] for row in range(r)]
        original_row = 0
        original_col = 0
        for row in range(0,r):
            for col in range(0,c):
                reshape_nums[row][col] = nums[original_row][original_col]
                if original_col+1 >= nums_col:
                    original_row += 1
                    original_col = 0
                else:
                    original_col += 1
        return reshape_nums

Solu = Solution()
nums = [[1, 2], [3, 4],[5,6]]
r = 2
c = 3
result = Solu.matrixReshape(nums,r,c)
print result



