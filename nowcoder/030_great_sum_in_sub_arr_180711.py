# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/11 17:14
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 030_great_sum_in_sub_arr_180711.py

"""
连续子数组最大和
"""

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return
        sum_arr = [array[0]]
        for i in range(1, len(array)):
            sum_arr.append(sum_arr[-1] + array[i])
        print(sum_arr)
        max_dif = sum_arr[0]
        min_pre = sum_arr[0]
        for i in range(1, len(array)):

            max_dif = max(max_dif, max(sum_arr[i], sum_arr[i] - min_pre))
            min_pre = min(min_pre, sum_arr[i])
        return max_dif

a = [6,-3,-2,7,-15,1,2,2]
# a = [-2,-8,-1,-5,-9]
print Solution().FindGreatestSumOfSubArray(a)

