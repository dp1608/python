# -*- coding: utf-8 -*-
# @StartTime : 2018/7/18 20:13
# @EndTime : 2018/7/18 20:26
# @Author  : Andy
# @Site    : 
# @File    : haoweilai_sum_180718.py
# @Software: PyCharm

"""
题目描述
输入两个整数 n 和 m，从数列1，2，3.......n 中随意取几个数,使其和等于 m ,要求将其中所有的可能组合列出来
输入描述:
每个测试输入包含2个整数,n和m
输出描述:
按每个组合的字典序排列输出,每行输出一种组合
示例1
输入

5 5
输出

1 4
2 3
5
"""

# s = raw_input()
s = "5 5"
ll = s.strip().split()
n, m = int(ll[0]), int(ll[1])

num = [i + 1 for i in range(n)]
# print(num)
res = []

def sum1(num, m, temp):
    if not num and m > 0:
        return
    if m == 0:
        res.append(temp)
        return
    for i in range(len(num)):
        sum1( num[i + 1:], m - num[i], temp + [num[i]])


sum1(num, m, [])
# print([1,2,4] + [123,4])
# print(res)
for s in res:
    print(" ".join(map(str, s)))


