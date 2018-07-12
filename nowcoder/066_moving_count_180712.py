# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/12 10:00
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 066_moving_count_180712.py

"""
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

"""

# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here

        if rows == 0 or cols == 0:
            return 0
        num = [[0 for _ in range(cols) ]for jjj in range(rows)]

        def verify(row, col):
            temp = 0
            s_row = str(row)
            s_col = str(col)
            for char in s_row:
                temp += int(char)
            for char in s_col:
                temp += int(char)
            if temp > threshold:
                return False
            else:
                return True

        res = 0

        def dfs(res, row, col):
            if row >= rows or col >= cols:
                return
            if num[row][col]:
                return
            if verify(row, col):
                num[row][col] = 1
                dfs(res, row + 1, col)
                dfs(res, row, col + 1)
            else:
                return

        dfs(res, 0, 0)
        # for i in range(rows):
        #     res += dfs(0, i, 0)
        # return res
        # print(num)
        res1 = 0
        for i in range(rows):
            res += sum(num[i])
        # return sum(num[i for i in range(rows)])
        return res

print(Solution().movingCount(10, 1, 100))
# print(Solution().movingCount(15, 20, 20))