# -*- coding: utf-8 -*-
# @StartTime : 10/18/2017 14:45
# @EndTime   : 10/18/2017 14:50
# @Author    : Andy
# @Site      : 
# @File      : 171018pascal's_triangleII.py
# @Software  : PyCharm

"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[List[int]]
        """
        # nums = []
        def generate(self, i, last_result):
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
        for i in range(rowIndex + 1):
            row_result = generate(self,i, row_result)
            # nums.append(row_result)
        return row_result

So = Solution()
print So.getRow(3)
print So.getRow(0)