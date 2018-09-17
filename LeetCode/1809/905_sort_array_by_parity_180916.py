# -*- coding: utf-8 -*-
# @StartTime : 2018/9/16 9:32
# @EndTime : 2018/9/16 9:32
# @Author  : Andy
# @Site    : 
# @File    : 905_sort_array_by_parity_180916.py
# @Software: PyCharm


"""
给定一个非负整数数组 A，返回一个由 A 的所有偶数元素组成的数组，后面跟 A 的所有奇数元素。

你可以返回满足此条件的任何数组作为答案。



示例：

输入：[3,1,2,4]
输出：[2,4,3,1]
输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。


提示：

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def jishu(n):
            if n & 1:
                return True
            else:
                return False

        def swap(A, l, r):
            temp = A[l]
            A[l] = A[r]
            A[r] = temp
        if not A:
            return []
        size = len(A)
        l = 0
        r = size - 1
        while jishu(A[r]) and r > 0:
            r -= 1
        while not jishu(A[l]) and l < size - 1:
            l += 1
        while l < r and l < size and r >= 0:
            if not jishu(A[l]):
                l += 1
                continue
            if jishu(A[r]):
                r -= 1
                continue
            swap(A, l, r)

        return A

A = [3,1,2,4]
print(Solution().sortArrayByParity(A))