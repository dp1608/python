# -*- coding: utf-8 -*-
# @StartTime : 2018/8/12 14:08
# @EndTime : 2018/8/12 14:08
# @Author  : Andy
# @Site    : 
# @File    : now_coder_0812_tengxun2.py
# @Software: PyCharm

"""
小Q最近遇到了一个难题：把一个字符串的大写字母放到字符串的后面，各个字符的相对位置不变，且不能申请额外的空间。
你能帮帮小Q吗？


输入描述:

输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.




输出描述:

对于每组数据，输出移位后的字符串。


输入例子1:
AkleBiCeilD

输出例子1:
kleieilABCD
"""
import sys
def swap(i,j,s):
    temp = s[j]
    s[i+1:j+1] =s[i:j]
    s[i] = temp
    return s

res = []

while 1:
    s = sys.stdin.readline().strip()
    if not s:
        break
    ls = list(s)
    index = -1
    for i in range(len(s)):
        if ord('a') <= ord(ls[i]) <= ord('z'):
            index += 1
            ls = swap(index,i,ls)
    res.append("".join(ls))
for i in range(len(res)):
    print(res[i])


