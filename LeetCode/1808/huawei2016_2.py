# -*- coding: utf-8 -*-
# @StartTime : 2018/8/12 16:00
# @EndTime : 2018/8/12 16:00
# @Author  : Andy
# @Site    : 
# @File    : huawei2016_2.py
# @Software: PyCharm

"""
开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。
处理:
1.记录最多8条错误记录，对相同的错误记录(即文件名称和行号完全匹配)只记录一条，错误计数增加；(文件所在的目录不同，文件名和行号相同也要合并)
2.超过16个字符的文件名称，只记录文件的最后有效16个字符；(如果文件名不同，而只是文件名的后16个字符和行号相同，也不要合并)
3.输入的文件可能带路径，记录文件名称不能带路径

输入描述:
一行或多行字符串。每行包括带路径文件名称，行号，以空格隔开。

    文件路径为windows格式

    如：E:\V1R2\product\fpgadrive.c 1325


输出描述:
将所有的记录统计并将结果输出，格式：文件名代码行数数目，一个空格隔开，如: fpgadrive.c 1325 1

    结果根据数目从多到少排序，数目相同的情况下，按照输入第一次出现顺序排序。

    如果超过8条记录，则只输出前8条记录.

    如果文件名的长度超过16个字符，则只输出后16个字符

输入例子1:
E:\V1R2\product\fpgadrive.c 1325

输出例子1:
fpgadrive.c 1325 1
"""

# import sys
#
# file_name = []
# hanghao = []
# c = []
# while 1:
#     line = sys.stdin.readline().strip()
#     if not line:
#         break
#     s0 = line.split()[0].split('\\')[-1]
#     s1 = int(line.split()[1])
#     if s0 in file_name:
#         pos = False
#         for index in range(len(file_name)):
#             if file_name[index] == s0:
#                 if hanghao[index] == s1:
#                     c[index] += 1
#                     pos = True
#         if not pos:
#             file_name.append(s0)
#             hanghao.append(s1)
#             c.append(1)
#     else:
#         file_name.append(s0)
#         hanghao.append(s1)
#         c.append(1)
#
# paixu = {}
# for i in range(len(file_name)):
#     ss = str(file_name) + ' ' + str(hanghao)
# # print(file_name)
# res = ''
# for i in range(min(8, len(file_name))):
#     res += ("".join(list(file_name[i])[-16:]) + ' ' + str(hanghao[i]) + ' ' + str(c[i]) + ' ')
#
# print(res)




import sys

file_name = []
# hanghao = []
c = []
while 1:
    line = sys.stdin.readline().strip()
    if not line:
        break
    s0 = line.split()[0].split('\\')[-1]
    s1 = line.split()[1]
    ss = s0 + '@' + s1
    if ss in file_name:
        pos = False
        index = file_name.index(ss)
        c[index] += 1
    else:
        file_name.append(ss)
        # hanghao.append(s1)
        c.append(1)

dict_s = {}
for i in range(len(file_name)):
    dict_s[file_name[i]] = c[i]

res_l = sorted(dict_s.items(), key=lambda x: x[1], reverse=True)
# print(file_name)
res = ''
for i in range(min(8, len(res_l))):
    temp1, temp2 = res_l[i]
    temp = temp1.split('@')
    s = "".join(list(temp[0])[-16:]) + ' ' + temp[1] + ' ' + str(temp2) + ' '
    # print(s)
    res += s
print(res)




