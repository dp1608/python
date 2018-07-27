# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/27 11:37
# @End_time:  2018/7/27 11:45
# @Author  : Andy
# @Site    : 
# @File    : 142_linked_list_cycleII_180727.py


"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        slow = l1 + l2
        fast = l1 + n * (l2 + l3)+ l2
        slow * 2 = fast
        l1 + l2 = n * (l2 + l3)
        cycle = l2 + l3
        """

        if not head:
            return None
        fast = head
        slow = head

        while fast:
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
            slow = slow.next
            if fast == slow:
                break
        if not fast:
            return None
        now = head

        while now != fast:
            now = now.next
            fast = fast.next
        return now
