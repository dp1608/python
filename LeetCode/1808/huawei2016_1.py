# -*- coding: utf-8 -*-
# @StartTime : 2018/8/12 15:47
# @EndTime : 2018/8/12 15:47
# @Author  : Andy
# @Site    : 
# @File    : huawei2016_1.py
# @Software: PyCharm

"""
老师想知道从某某同学当中，分数最高的是多少，现在请你编程模拟老师的询问。当然，老师有时候需要更新某位同学的成绩.
输入描述:
输入包括多组测试数据。
每组输入第一行是两个正整数N和M（0 < N <= 30000,0 < M < 5000）,分别代表学生的数目和操作的数目。
学生ID编号从1编到N。
第二行包含N个整数，代表这N个学生的初始成绩，其中第i个数代表ID为i的学生的成绩
接下来又M行，每一行有一个字符C（只取‘Q’或‘U’），和两个正整数A,B,当C为'Q'的时候, 表示这是一条询问操作，他询问ID从A到B（包括A,B）的学生当中，成绩最高的是多少
当C为‘U’的时候，表示这是一条更新操作，要求把ID为A的学生的成绩更改为B。


输出描述:
对于每一次询问操作，在一行里面输出最高成绩.

输入例子1:
5 7
1 2 3 4 5
Q 1 5
U 3 6
Q 3 4
Q 4 5
U 4 5
U 2 9
Q 1 5

输出例子1:
5
6
5
9
"""

import sys

res = []

def max(arr):
    if not arr:
        return
    res = arr[0]
    for i in range(len(arr)):
        if res < arr[i]:
            res = arr[i]
    return res


while 1:
    line = sys.stdin.readline().strip()
    if not line:
        break
    n, m = map(int, line.split())
    rank = map(int, sys.stdin.readline().strip().split())
    for _ in range(m):
        line = sys.stdin.readline().strip().split()
        a = int(line[1])
        b = int(line[2])
        if line[0] == 'Q':
            if a > b:
                temp = a
                a = b
                b = temp
            res.append(max(rank[a-1:b]))
        if line[0] == 'U':
            rank[a-1] = b

for i in range(len(res)):
    print(res[i])

