# -*- coding: utf-8 -*-
# @StartTime : 2018/7/25 23:09
# @EndTime : 2018/7/25 23:09
# @Author  : Andy
# @Site    : 
# @File    : mobai_zifuchuan_180725.py
# @Software: PyCharm


"""
小摩手里有一个字符串A，小拜的手里有一个字符串B，B的长度大于等于A，所以小摩想把A串变得和B串一样长，这样小拜就愿意和小摩一起玩了。
而且A的长度增加到和B串一样长的时候，对应的每一位相等的越多，小拜就越喜欢。比如"abc"和"abd"对应相等的位数为2，为前两位。
小摩可以在A的开头或者结尾添加任意字符，使得长度和B一样。现在问小摩对A串添加完字符之后，不相等的位数最少有多少位？

输入描述:
第一行 为字符串A，第二行 为字符串B，
A的长度小于等于B的长度，B的长度小于等于100。
字符均为小写字母。


输出描述:
输出一行整数表示A串添加完字符之后，A B 不相等的位数最少有多少位？

输入例子1:
abe
cabc

输出例子1:
1
"""

# s1 = raw_input()
# s2 = raw_input()
s1 = "abe"
s2 = "cabc"

size1 = len(s1)
size2 = len(s2)


def compared(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            count += 1
    return count

max_same = 0
for i in range(0, size2 - size1 + 1):
    temp = compared(s1, s2[i:size1 + i])
    if temp > max_same:
        max_same = temp

print(size1 - max_same)