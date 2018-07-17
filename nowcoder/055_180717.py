# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/17 16:52
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 055_180717.py

"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

"""

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None
        index = pHead
        tree = []
        while index:
            if index not in tree:
                tree.append(index)
                index = index.next
            else:
                return index
        return None