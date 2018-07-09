# -*- coding: utf-8 -*-
# @StartTime : 2018/7/4 9:44
# @EndTime : 2018/7/4 9:44
# @Author  : Andy
# @Site    : 
# @File    : 016_reverse__list_180704.py
# @Software: PyCharm
"""
输入一个链表，反转链表后，输出新链表的表头。
"""

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return pHead

        pre = pHead
        this = pre.next
        pre.next = None
        next = None
        while this:
            next = this.next
            this.next = pre
            pre = this
            this = next
        return pre

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
b = Solution().ReverseList(a)
print(b.val)
b = b.next
print(b.val)
b = b.next
print(b.val)
b = b.next
print(b.val)
b = b.next
print(b.val)


