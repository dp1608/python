# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/3 16:27
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 009_jump_floorII_180703.py
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number < 1:
            return 0
        if number == 1:
            return 1
        res = [1, 2]
        for i in range(2, number):
            temp = 1 + sum(res)
            res.append(temp)
        return res[-1]
