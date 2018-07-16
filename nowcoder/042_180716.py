# -*- coding: utf-8 -*-
# @StartTime : 2018/7/16 16:24
# @EndTime : 2018/7/16 16:24
# @Author  : Andy
# @Site    : 
# @File    : 042_180716.py
# @Software: PyCharm

"""
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出
"""

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return
        l = 0
        r = len(array) - 1
        res = []
        while l < r:
            if array[l] + array[r] > tsum:
                r -= 1
            elif array[l] + array[r] < tsum:
                l += 1
            else:
                return [array[l], array[r]]
        return None

arr = [1,2,4,7,11,16]
print(Solution().FindNumbersWithSum(arr, 10))

