# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/26 10:45
# @End_time: 2018/6/26 15:45
# @Author  : Andy
# @Site    : 
# @File    : 82_remove_duplicates_from_sorted_listII.py

"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        if not head.next:
            return head
        # first process head duplicates
        while head:
            if not head.next:
                return head
            if head.next.val == head.val:
                value = head.val
                head = head.next
                # pre_head = head
                while head:
                    if value == head.val:
                        head = head.next
                        continue
                    break
            else:
                break

        if not head:
            return head
        if not head.next:
            return head

        index = head.next
        pre_index = head
        pre_index.next = None
        value1 = head.val - 100
        while index:
            if index.val == value1:
                index = index.next
                continue
            if not index.next:
                pre_index.next = index
                pre_index = pre_index.next
                break
            if index.next.val == index.val:
                value1 = index.val
                index = index.next
                continue
            pre_index.next = index
            pre_index = pre_index.next
            index = index.next
        pre_index.next = None
        return head


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(3)
# e = ListNode(3)
a.next = b
b.next = c
c.next = d
# d.next = e

# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)
# d = ListNode(3)
# e = ListNode(4)
# f = ListNode(4)
# g = ListNode(5)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# f.next = g

res = Solution().deleteDuplicates(a)
print(res.val)
res = res.next
print(res.val)
res = res.next
print(res.val)

