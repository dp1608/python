# -*- coding: utf-8 -*-
# @Time    : 2017/4/2 20:38
# @Author  : Andy
# @E-mail  ：chendi@radi.ac.cn
# @Site    :
# @File    : Task2.py
# @Software: PyCharm

# 题目：给定一个数组A，按照特定要求，一行K列显示。
# you can write to stderr for debugging purposes, e.g.
# sys.stderr.write("this is a debug message\n")
import  sys
def solution(A, K):
    # write your code in Python 2.7
    N = len(A)
    row=0
    col=0
    if N<=K:
        row=1
        col=N
    else:
        row=(N+K-1)/K
        col=K

    max_A=max(A)
    max_len=lengthD(max_A)
    str_diag = '+'
    str_row = '-'
    for i in range(1,max_len):
        str_row+='-'
    str_col='|'

    for i in range(1,2*row):
        if i%2==1:
            for j in range(1,col+1):
                print str_diag,
                sys.stdout.softspace = 0
                print str_row,
                sys.stdout.softspace = 0
            print str_diag
        else:
            for j in range(1,col+1):
                numb=(i/2-1)*col+j
                print str_col,
                sys.stdout.softspace = 0
                print output_str(A[numb-1],max_len),
                sys.stdout.softspace = 0
            print str_col
    #print last one row
    last_index=(row-1)*col
    numb=last_index
    while numb != N:
        numb += 1
        print str_col,
        sys.stdout.softspace = 0
        print output_str(A[numb-1], max_len),
        sys.stdout.softspace = 0
    print str_col
    numb = last_index
    while numb != N:
        numb += 1
        print str_diag,
        sys.stdout.softspace = 0
        print str_row,
        sys.stdout.softspace = 0
    print str_diag

def output_str(M,max):
    i=lengthD(M)
    string=''
    for j in range(1,max-i+1):
        string+=' '
    string+=str(M)
    return string

def lengthD(num):
    lendig = 0
    while num != 0:
        num = num/10
        lendig += 1
    return lendig


A=[4,35,80,123,12345,44,8,5,24,3,22,555,555,452]
K=10
print 1,
print 2
print 3,4
solution(A,K)