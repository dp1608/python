# -*- coding: utf-8 -*-
# @StartTime : 2018/7/11 22:44
# @EndTime : 2018/7/11 22:44
# @Author  : Andy
# @Site    : 
# @File    : 035_inverse_pairs_180711.py
# @Software: PyCharm

"""
数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。
即输出P%1000000007
"""


# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0
        global count
        count = 0

        def merge(arr):
            global count
            if len(arr) <= 1:
                return arr
            mid = (len(arr)) // 2
            left = merge(arr[:mid])
            right = merge(arr[mid:])
            l = 0
            r = 0
            res = []
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    count += len(left) - l
                    r += 1
                res += left[l:]
                res += right[r:]
                return res

        rr = merge(data)
        # print(rr)
        return count

a = [1,2,3,4,5,6,7,0]
print(Solution().InversePairs(a))



