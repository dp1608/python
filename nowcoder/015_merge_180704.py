# -*- coding: utf-8 -*-
# @StartTime : 2018/7/4 9:56
# @EndTime : 2018/7/4 9:56
# @Author  : Andy
# @Site    : 
# @File    : 015_merge_180704.py
# @Software: PyCharm

"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        pre = ListNode(0)
        pointer = pre
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                pointer.next = pHead1
                pHead1 = pHead1.next
            else:
                pointer.next = pHead2
                pHead2 = pHead2.next
            pointer = pointer.next
        while pHead1:
            pointer.next = pHead1
            pHead1 = pHead1.next
            pointer = pointer.next
        while pHead2:
            pointer.next = pHead2
            pHead2 = pHead2.next
            pointer = pointer.next
        return pre.next

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(4)
b = ListNode(None)
# b.next = ListNode(4)
# b.next.next = ListNode(5)
head = Solution().Merge(a,b)
print(head.val)
head = head.next
print(head.val)
head = head.next
print(head.val)
head = head.next
print(head.val)
head = head.next
