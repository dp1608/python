# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/17 17:01
# @End_time: 2018/7/17 17:14
# @Author  : Andy
# @Site    : 
# @File    : 056_180717.py

"""
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None
        p_pre = ListNode(pHead.val - 1)
        p_pre.next = pHead
        val = p_pre.val - 1
        p_index = p_pre

        while pHead:
            if pHead.val == val:
                p_index.next = pHead.next
                pHead = pHead.next
            elif pHead.next and pHead.val == pHead.next.val:
                val = pHead.val
            else:
                p_index = p_index.next
                pHead = pHead.next
        return p_pre.next


a = ListNode(1)
b = ListNode(1)
c = ListNode(3)
d = ListNode(3)
e = ListNode(4)
f = ListNode(4)
g = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

res = (Solution().deleteDuplication(a))
print(res.val)
res = res.next
print(res.val)
res = res.next
print(res.val)
res = res.next


