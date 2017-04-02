# -*- coding: utf-8 -*-
# @Time    : 2017/4/2 20:38
# @Author  : Andy
# @E-mail  ：chendi@radi.ac.cn
# @Site    :
# @File    : Task1.py
# @Software: PyCharm

#判断一个数组，交换两个元素后，是否为排序好的数组，若本已排好序，则返回ture

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    judge = 0
    if judge_sorted(A):
        judge=1

    len_A = len(A)
    for i in range(1,len_A):
        for j in range(i+1,len_A+1):
            B=swap(A,i-1,j-1)
            if judge_sorted(B):
                judge=1
            B = swap(A,j-1, i-1)
    if judge:
        return True
    else:
        return False


def swap(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp
    return A

def judge_sorted(A):
    length=len(A)
    count1=0
    count2=0
    for i in range(1,length):
        if A[i-1]<=A[i]:
            count1+=1
        if A[i-1]>=A[i]:
            count2+=1
    if count1==length-1:
        return 1
    elif count2==length-1:
        return 1
    else:
        return 0


A=[1,3,3,7,5,6,8]

print solution(A)

#print judge_sorted(A)
