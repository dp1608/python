# -*- coding: utf-8 -*-
# @Start_Time : 2018/6/28 16:53
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 98_invalidate_binary_search_tree_180628.py

"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        inorder_list = []
        if not root:
            return True
        def inorder(root):
            if root.left:
                inorder(root.left)
            inorder_list.append(root.val)
            if root.right:
                inorder(root.right)

        inorder(root)
        # print(inorder_list)
        for i in range(len(inorder_list) - 1):
            if inorder_list[i] < inorder_list[i + 1]:
                continue
            else:
                return False
        return True

a = TreeNode(2)
b = TreeNode(1)
c = TreeNode(3)
a.left = b
a.right = c
print(Solution().isValidBST(a))