# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/26 15:14
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 83_remove_duplicates_from_sorted_list.py

"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
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
        dummy = head
        while head:
            if head.next and head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next

        return dummy