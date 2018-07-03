# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/3 15:34
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 003_tail_to_head_print_180703.py

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        stack = []
        if not listNode:
            return []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        stack = stack[::-1]
        return stack