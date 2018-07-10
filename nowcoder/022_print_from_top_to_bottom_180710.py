# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/10 10:13
# @End_time: 2018/7/10 10:24
# @Author  : Andy
# @Site    : 
# @File    : 022_print_from_top_to_bottom_180710.py

"""
从上往下打印出二叉树的每个节点，同层节点从左至右打印。

"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        res = []
        deque = [root]
        while deque:
            now = deque[0]
            if now.left:
                deque.append(now.left)
            if now.right:
                deque.append(now.right)
            res.append(now.val)
            del deque[0]
        return res
