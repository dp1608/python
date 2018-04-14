# -*- coding: utf-8 -*-
# @StartTime : 2018/4/14 10:41
# @EndTime : 2018/4/14 10:41
# @Author  : Andy
# @Site    : 
# @File    : quick_sort.py
# @Software: PyCharm


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r, 1):
        if A[j] < x:
            i = i + 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    tmp2 = A[i + 1]
    A[i + 1] = x
    A[r] = tmp2
    return i + 1


A = [2, 8, 7, 1, 3, 5, 6, 4]
quick_sort(A, 0, len(A) - 1)
print(A)

