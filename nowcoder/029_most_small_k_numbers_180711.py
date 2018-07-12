# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/11 11:02
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 029_most_small_k_numbers_180711.py

"""
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here

        def swap(arr, a, b):
            temp = arr[a]
            arr[a] = arr[b]
            arr[b] = temp

        def partition(arr, left, right):
            xr = arr[right]
            index = left
            for i in range(left, right):
                if arr[i] < xr:
                    swap(arr, i, index)
                    index += 1
            swap(arr, right, index)
            return index

        size = len(tinput)
        if size < k:
            return []
        left = 0
        right = len(tinput) - 1

        while 1:
            q = partition(tinput, left, right)
            if q < k - 1:
                left = q + 1
                continue
            elif q > k - 1:
                right = q - 1
                continue
            else:
                break
        res = tinput[0:k]
        res.sort()
        return res


a = [4,5,1,6,2,7,3,8,1,2]
print(Solution().GetLeastNumbers_Solution(a,4))
