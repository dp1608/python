# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/27 16:36
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 92_reverse_linked_list_II.py

"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
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


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        Input: 1->2->3->4->5->NULL, m = 2, n = 4
          step1: 1  3  2   4  5
                lm   head  rn
          step2: 1  4  3  2
                lm
        Output: 1->4->3->2->5->NULL
        """
        head_sentinel = ListNode(0)
        head_sentinel.next = head
        l_m = head_sentinel
        while m != 1:
            l_m = head
            head = head.next
            m -= 1
            n -= 1

        while n != 1 and head.next:
            n -= 1
            r_n = head.next.next  # 4 5
            temp = l_m.next
            l_m.next = head.next   # 3 4
            head.next = r_n   # 4 5
            l_m.next.next = temp  # 2
        return head_sentinel.next

a = [1,2,3,4,5]
# a = [1,2,3,4,5,6,7,8,9]
link_a = create_linklist(a)
res_a = Solution().reverseBetween(link_a, 1, 5)
print(print_link(res_a))

