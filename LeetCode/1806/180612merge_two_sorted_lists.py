# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/12 9:49
# @End_time: 2018/6/12 10:30
# @Author  : Andy
# @Site    : 
# @File    : 180612merge_two_sorted_lists.py

"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together
the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_index = l1
        l2_index = l2
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            res = ListNode(l2.val)
            l2 = l2.next
        else:
            res = ListNode(l1.val)
            l1 = l1.next
        ret = res
        while l1 and l2:
            if l1.val > l2.val:
                res.next = l2
                l2 = l2.next
                res = res.next
            else:
                res.next = l1
                l1 = l1.next
                res = res.next
        while l2:
            res.next = l2
            l2 = l2.next
            res = res.next
        while l1:
            res.next = l1
            l1 = l1.next
            res = res.next
        return ret

s1 = ListNode(2)
# s2 = ListNode(2)
# s3 = ListNode(4)
# s1.next = s2
# s2.next = s3
#
m1 = ListNode(1)
# m2 = ListNode(3)
# m3 = ListNode(4)
# m1.next = m2
# m2.next = m3

ret = Solution().mergeTwoLists(s1, m1)
print(ret.val)
print(ret.next.val)
ret = ret.next.next

