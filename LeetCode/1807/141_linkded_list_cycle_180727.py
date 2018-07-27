# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/27 10:23
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 141_linkded_list_cycle_180727.py


"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?


"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        fast = head.next
        slow = head

        while fast:
            if fast == slow:
                return True
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
            slow = slow.next

        return False
