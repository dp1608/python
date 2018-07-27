# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/27 11:47
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 143_reorder_list_180727.py


"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        list_link = []
        index = head
        while index:
            list_link.append(index)
            index = index.next

        pre = head
        order = 1
        while list_link:
            if not list_link:
                pre.next = None
                pre = pre.next
            if order == 1:
                pre.next = list_link[0]
                del list_link[0]
                pre = pre.next
            elif order == -1:
                pre.next = list_link.pop()
                pre = pre.next
            order = -order
        pre.next = None
        # return head


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
res = Solution().reorderList(a)
print(res.val)
res = res.next
print(res.val)
res = res.next
print(res.val)
res = res.next
print(res.val)
res = res.next
print(res.val)
res = res.next
print(res.val)