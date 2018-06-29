# -*- coding: utf-8 -*-
# @StartTime : 2018/6/29 10:37
# @EndTime : 2018/6/29 10:40
# @Author  : Andy
# @Site    : 
# @File    : 104_maximum_depth_of_binary_tree180629.py
# @Software: PyCharm

"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        def max_depth(root):
            if not root:
                return 0
            return max(1 + max_depth(root.left), 1 + max_depth(root.right))
        return max_depth(root)


