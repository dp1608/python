# -*- coding: utf-8 -*-
# @StartTime : 2018/7/24 21:45
# @EndTime : 2018/7/24 21:45
# @Author  : Andy
# @Site    : 
# @File    : taobao_jieli_180724.py
# @Software: PyCharm


# n = int(raw_input())
# m = int(raw_input())
# s = raw_input().split()

n = 3
m = 2
map1 = [[0, 2, 3], [2, 0, 1], [3, 1, 0]]

# map1 = [[0 for _ in range(n)] for _i in range(n)]
res = [[0x99999999 for _ in range(n)] for _i in range(n)]

# for i in range(n):
#     ll = map(int, raw_input().split())
#     print(ll)
    # for j in range(n):
    #     map1[i][j] = ll[j]


def dfs(i_0, j_target, i, count, k):
    if k == 0 and i == j_target:
        if res[i_0][j_target] > count:
            res[i_0][j_target] = count
        else:
            return
    if k == 0:
        return
    for index in range(n):
        if i != index:
            dfs(i_0, j_target, index, count + map1[i][index], k - 1)


for i in range(n):
    for j in range(i, n):
        dfs(i, j, i, 0, m)

for i in range(n):
    for j in range(i):
        res[i][j] = res[j][i]

for i in range(n):
    println = ""
    for j in range(n):
        println += str(res[i][j]) + " "
    print(println)
