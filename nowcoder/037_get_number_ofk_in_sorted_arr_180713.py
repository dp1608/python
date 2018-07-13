# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/13 16:15
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 037_get_number_ofk_in_sorted_arr_180713.py

"""
统计一个数字在排序数组中出现的次数。

"""

# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        res = 0
        size = len(data)
        left = 0
        right = size
        while right - left > 0:
            mid = (left + right) // 2
            if data[mid] == k:
                break
            elif data[mid] > k:
                right = mid
            else:
                left = mid

        if data[mid] == k:
            res += 1
            l1 = mid - 1
            l2 = mid + 1
            while l1 >= 0 and data[l1] == k:
                res += 1
                l1 -= 1
            while l2 < size and data[l2] == k:
                res += 1
                l2 += 1

        return res

print(Solution().GetNumberOfK([0,0,0,0,1,2,3,5,5,5,6,6,6,6],0))

