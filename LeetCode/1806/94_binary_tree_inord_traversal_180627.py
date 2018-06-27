# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/27 17:59
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 94_binary_tree_inord_traversal_180627.py

"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def inorder_tree(root, res):
            if root:
                res = inorder_tree(root.left, res)
                res.append(root.val)
                res = inorder_tree(root.right, res)
                return res
            else:
                return res



        res = inorder_tree(root, [])
        return res


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.right = b
b.left = c
res = Solution().inorderTraversal(a)
print(res)


