# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/10 16:43
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 028_more_than_half_180710.py

"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

"""

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        size = len(numbers)

        def swap(arr, i, j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

        def partition(arr, left, right):
            index = left
            xr = arr[right]
            for i in range(left, right, 1):
                if arr[i] < xr:
                    swap(arr, i, index)
                    index += 1
            swap(arr, right, index)
            return index

        def verify(arr, n):
            if arr.count(n) > size // 2:
                return True
            else:
                return False

        left = 0
        right = size - 1
        mid = (size - 1) // 2
        q = 0
        while right - left > 0:
            q = partition(numbers, left, right)
            if q == mid:
                if verify(numbers, numbers[q]):
                    return numbers[q]
                else:
                    return 0
            elif q < mid:
                left = q + 1
                continue
            elif q > mid:
                right = q - 1
                continue

        if verify(numbers, numbers[q]):
            return numbers[q]
        else:
            return 0

#
a = [1,2,3,2,2,2,5,4,2]
a = [1]
#
#
# def swap(arr, i, j):
#     temp = arr[i]
#     arr[i] = arr[j]
#     arr[j] = temp
#
# def partition(arr, left, right):
#     index = left
#     xr = arr[right]
#     for i in range(left, right, 1):
#         if arr[i] < xr:
#             swap(arr, i, index)
#             index += 1
#     swap(arr, right, index)
#     return index - 1

b = [1,2,3,5,6,7,4]
# print(partition(b,0,6))
print(Solution().MoreThanHalfNum_Solution(a))
