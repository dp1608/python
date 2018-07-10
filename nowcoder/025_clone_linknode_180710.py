# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/10 14:50
# @End_time: 2018/7/10 15:46
# @Author  : Andy
# @Site    : 
# @File    : 025_clone_linknode_180710.py

"""
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

"""


# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

a = RandomListNode(1)
b = RandomListNode(2)
c = RandomListNode(3)
d = RandomListNode(4)
e = RandomListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
a.random = c
b.random = e
d.random = b


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        p_pre = pHead
        while p_pre:
            current = p_pre.next
            new = RandomListNode(p_pre.label)
            new.next = current
            # new.random = p_pre.random
            p_pre.next = new
            p_pre = current
        p_pre = pHead
        while p_pre:
            p_new = p_pre.next
            if p_pre.random:
                p_new.random = p_pre.random.next
            p_pre = p_pre.next.next


        p_indicator = pHead
        p_clone = pHead.next
        while p_indicator:
            copy_node = p_indicator.next
            p_indicator_next = copy_node.next
            p_indicator.next = p_indicator_next
            if p_indicator_next:
                copy_node.next = p_indicator_next.next
            p_indicator = p_indicator_next
        return p_clone


root = Solution().Clone(a)
print(root.label)
root = root.next
print(root.label)
root = root.next
print(root.label)
root = root.next
print(root.label)
root = root.next
print(root.label)
