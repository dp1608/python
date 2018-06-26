# -*- coding: utf-8 -*-
# @StartTime : 2018/6/20 23:07
# @EndTime : 2018/6/20 23:07
# @Author  : Andy
# @Site    : 
# @File    : 61_rotate_list_180620.py
# @Software: PyCharm

"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        if k == 0:
            return head
        count = 0
        point = head
        while point:
            point = point.next
            count += 1

        k = k % count
        res = head
        l = head
        r = head
        for i in range(k):
            r = r.next
        while r.next:
            l = l.next
            r = r.next
        r.next = head
        head = l.next
        l.next = None
        return head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
a = Solution().rotateRight(a, 2)
print(a.val)
a = a.next
print(a.val)
a = a.next
print(a.val)
a = a.next
print(a.val)
a = a.next
print(a.val)


