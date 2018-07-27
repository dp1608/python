# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/27 16:10
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 144_binary_tree_preorder_traversal_180727.py


"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal2(self, root):
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def pre_order(root):
            if not root:
                return
            res.append(root.val)
            pre_order(root.left)
            pre_order(root.right)

        pre_order(root)
        return res