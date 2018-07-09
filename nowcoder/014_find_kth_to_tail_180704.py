# -*- coding: utf-8 -*-
# @StartTime : 2018/7/4 9:37
# @EndTime : 2018/7/4 9:37
# @Author  : Andy
# @Site    : 
# @File    : 014_find_kth_to_tail_180704.py
# @Software: PyCharm

"""
输入一个链表，输出该链表中倒数第k个结点。

"""

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        slow = head
        fast = head
        while k and fast:
            fast = fast.next
            k -= 1
        if k:
            return None
        while fast:
            fast = fast.next
            slow = slow.next
        return slow