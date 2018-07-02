# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/2 11:06
# @End_time:  2018/7/2 11:21
# @Author  : Andy
# @Site    : 
# @File    : 111_minimum_depth_of_binary_tree_180702.py

"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def dfs(root):
            if not root.left and not root.right:
                return 1
            elif not root.left:
                return dfs(root.right) + 1
            elif not root.right:
                return dfs(root.left) + 1
            else:
                return min(dfs(root.left) + 1, dfs(root.right) + 1)
        return dfs(root)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().minDepth(root))