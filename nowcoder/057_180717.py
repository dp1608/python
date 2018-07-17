# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/17 17:30
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 057_180717.py

"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""

# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        # write code here

        def next_core(root):
            # if root.right:
            #     return next_root(root.right)
            if not root:
                return None
            if root.next.left == root:
                return root.next
            else:
                return next_core(root.next)


        def next_root(root):
            if root.left:
                return next_root(root.left)
            else:
                return root

        # return next_core(pNode)
        if pNode.right:
            return next_root(pNode.right)
        else:
            return next_core(pNode)


# "{8,6,10,5,7,9,11},7"
root = TreeLinkNode(8)
root.left = TreeLinkNode(6)
root.left.next = root
root.right = TreeLinkNode(10)
root.right.next = root
root.left.right = TreeLinkNode(7)
root.left.right.next = root.left
root.left.left = TreeLinkNode(5)
root.left.right.next = root.left
root.right.left = TreeLinkNode(9)
root.right.left.next = root.right
root.right.right = TreeLinkNode(10)
root.right.right.next = root.right
print(Solution().GetNext(root.left.right).val)