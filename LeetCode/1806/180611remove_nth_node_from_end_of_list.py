# -*- coding: utf-8 -*-
# @StartTime : 2018/6/11 20:42
# @EndTime : 2018/6/11 20:42
# @Author  : Andy
# @Site    : https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802/3-short-Python-solutions
# @File    : 180611remove_nth_node_from_end_of_list.py
# @Software: PyCharm


"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

s1 = ListNode(1)
s2 = ListNode(2)
# s1.val = 1
# s1.next = s2
# s2.val = 2
print(Solution().removeNthFromEnd(s1, 1).val)


