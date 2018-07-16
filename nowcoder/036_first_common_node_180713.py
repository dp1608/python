# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/13 15:56
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 036_first_common_node_180713.py

"""
输入两个链表，找出它们的第一个公共结点。
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None

        p1 = pHead1
        p2 = pHead2

        l1 = 0
        l2 = 0

        while p1:
            l1 += 1
            p1 = p1.next

        while p2:
            l2 += 1
            p2 = p2.next

        p1 = pHead1
        p2 = pHead2

        if l1 > l2:
            for _ in range(l1 - l2):
                p1 = p1.next
        elif l1 < l2:
            for _ in range(l2 - l1):
                p2 = p2.next

        while p1:
            if p1 == p2:
                return p1
            else:
                p1 = p1.next
                p2 = p2.next

        return None