# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/3 16:21
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 008_jump_floor_180703.py
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number < 1:
            return 0
        if number == 1:
            return 1
        res = [1, 2]
        for i in range(2, number):
            temp = res[-1] + res[-2]
            res.append(temp)
        print(res)
        return res[-1]

print(Solution().jumpFloor(5))
