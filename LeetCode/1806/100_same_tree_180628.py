# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/28 17:01
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 100_same_tree_180628.py

"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def pre_order(root, res):
            res.append(root.val)
            if root.left:
                pre_order(root.left, res)
            else:
                res.append('null')
            if root.right:
                pre_order(root.right, res)
            else:
                res.append('null')
            return res

        def in_order(root, res):
            if root.left:
                pre_order(root.left, res)
            else:
                res.append('null')
            res.append(root.val)
            if root.right:
                pre_order(root.right, res)
            else:
                res.append('null')
            return res

        if not p and not q:
            return True
        if not p or not q:
            return False

        p_pre = pre_order(p, [])
        p_in = in_order(p, [])
        q_pre = pre_order(q, [])
        q_in = in_order(q, [])
        if p_pre != q_pre:
            return False
        if p_in != q_in:
            return False
        return True

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(3)
q.right = TreeNode(3)
print(Solution().isSameTree(p,q))
