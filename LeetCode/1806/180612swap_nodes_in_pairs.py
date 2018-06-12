# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/12 15:49
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 180612swap_nodes_in_pairs.py

"""
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = head
        if not head:
            return
        while head.next:
            temp = head.val
            head.val = head.next.val
            head.next.val = temp
            if head.next:
                head = head.next
            if head.next:
                head = head.next

        return res

s1 = ListNode(1)
s2 = ListNode(2)
s3 = ListNode(3)
s4 = ListNode(4)
s1.next = s2
s2.next = s3
s3.next = s4
head = Solution().swapPairs(s1)

print(head.val)
head = head.next
print(head.val)
head = head.next
print(head.val)
head = head.next
print(head.val)


