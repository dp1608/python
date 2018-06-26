# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/26 15:34
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 86_partition_list.py

"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def create_linklist(a):
    """
    :param a: List
    :return: ListNode
    """
    sentinel = ListNode(0)
    head = sentinel
    for i in range(len(a)):
        num = a[i]
        linka = ListNode(num)
        head.next = linka
        head = head.next
    return sentinel.next


def print_link(head):
    a = []
    while head:
        a.append(head.val)
        head = head.next
    return a

# 问题所在：1.空间复杂度，由于多创建了一个链表，空间复杂度较高，所以，思考原链表上修改


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        pre = sentinel = ListNode(0)
        slow = head
        fast = head
        while fast:
            if fast.val < x:
                sentinel.next = ListNode(fast.val)
                sentinel = sentinel.next
                fast = fast.next
            else:
                fast = fast.next

        while slow:
            if slow.val < x:
                slow = slow.next
            else:
                sentinel.next = ListNode(slow.val)
                sentinel = sentinel.next
                slow = slow.next
        return pre.next

    # def partition(self, head, x):
    #     h1 = l1 = ListNode(0)
    #     h2 = l2 = ListNode(0)
    #     while head:
    #         if head.val < x:
    #             l1.next = head
    #             l1 = l1.next
    #         else:
    #             l2.next = head
    #             l2 = l2.next
    #         head = head.next
    #     l2.next = None
    #     l1.next = h2.next
    #     return h1.next

a = [1,4,3,2,5,2]
link_a = create_linklist(a)
res = Solution().partition(link_a, 3)
print(print_link(res))