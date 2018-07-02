# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/2 16:41
# @End_time:  2018/7/2 16:55
# @Author  : Andy
# @Site    : 
# @File    : 120_triangle_280702.py
"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return
        row = len(triangle)
        if row == 1:
            return triangle[0][0]
        minum_pre = [triangle[0][0]]

        def dyprogram(minum_pre):
            minum_this = []
            index = len(minum_pre)
            for i in range(index + 1):
                if i == 0:
                    minum_this.append(minum_pre[i] + triangle[index][i])
                    continue
                if i == index:
                    minum_this.append(minum_pre[i - 1] + triangle[index][i])
                    continue
                minum_this.append(min(minum_pre[i], minum_pre[i - 1]) + triangle[index][i])
            return minum_this

        for _ in range(1, row):
            minum_pre = dyprogram(minum_pre)
        print(minum_pre)
        return min(minum_pre)


a = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(Solution().minimumTotal(a))



