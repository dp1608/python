# -*- coding: utf-8 -*-
# @StartTime : 2018/8/12 14:34
# @EndTime : 2018/8/12 14:34
# @Author  : Andy
# @Site    : 
# @File    : now_code_0812_tengxun3.py
# @Software: PyCharm

"""
小Q今天在上厕所时想到了这个问题：有n个数，两两组成二元组，相差最小的有多少对呢？相差最大呢？


输入描述:

 输入包含多组测试数据。

 对于每组测试数据：

 N - 本组测试数据有n个数

 a1,a2...an - 需要计算的数据

 保证:

 1<=N<=100000,0<=ai<=INT_MAX.




输出描述:

对于每组数据，输出两个数，第一个数表示差最小的对数，第二个数表示差最大的对数。


输入例子1:
6
45 12 45 32 5 6

输出例子1:
1 2
"""

import sys
res = []


while 1:
    line = sys.stdin.readline().strip()
    if not line:
        break
    n = int(line)
    arr = map(int, sys.stdin.readline().strip().split())
    if len(arr) <= 2:
        res.append(str(1)+' ' + str(1))
    if 1:
        max_num = max(arr)
        min_num = min(arr)
        max_diff1 = arr.count(max_num)
        max_diff2 = arr.count(min_num)
        # max_diff = zuhe(max_diff1 + max_diff2, max_diff1)
        max_diff = max_diff1 * max_diff2

    min_diff = abs(arr[1] - arr[0])
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                continue
            if abs(arr[i]-arr[j]) < min_diff:
                min_diff = abs(arr[i]-arr[j])

    min_ = 0
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if i==j:
                continue
            if abs(arr[i]-arr[j]) == min_diff:
                min_ += 1
    res.append(str(min_)+ ' ' + str(max_diff))

for ii in range(len(res)):
    print(res[ii])
