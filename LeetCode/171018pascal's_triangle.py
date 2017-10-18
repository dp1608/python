# -*- coding: utf-8 -*-
# @StartTime : 10/18/2017 14:20
# @EndTime   : 10/18/2017 14:42
# @Author    : Andy
# @Site      : 
# @File      : 171018pascal's_triangle.py
# @Software  : PyCharm

"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        nums = []
        def generate1(self, i, last_result):
            row_result = []
            if i == 0:
                row_result = [1]
            else:
                for j in range(i+1):
                    if j ==0 or j == i:
                        row_result.append(1)
                    else:
                        row_result.append(last_result[j-1] + last_result[j])
            return row_result

        row_result = []
        for i in range(numRows):
            row_result = generate1(self,i, row_result)
            nums.append(row_result)
        return nums

So = Solution()
print So.generate(5)
print So.generate(0)