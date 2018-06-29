# -*- coding: utf-8 -*-
# @StartTime : 2018/6/29 19:45
# @EndTime : 2018/6/29 19:45
# @Author  : Andy
# @Site    : 
# @File    : 110_balanced_binary_tree_180629.py
# @Software: PyCharm

"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        def dfs_max(root):
            if not root:
                return 0
            return max(1 + dfs_max(root.left), 1 + dfs_max(root.right))

        left = dfs_max(root.left)
        right = dfs_max(root.right)
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)






root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().isBalanced(root))