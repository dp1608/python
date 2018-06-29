# -*- coding: utf-8 -*-
# @StartTime : 2018/6/29 10:46
# @EndTime : 2018/6/29 11:00
# @Author  : Andy
# @Site    : 
# @File    : 105_construct_binary_tree_from_preorder_and_inorder_traversal_180629.py
# @Software: PyCharm

"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return
        # root = TreeNode(preorder[0])

        def dfs(preorder, inorder):
            if not preorder:
                return None
            n = preorder[0]
            root = TreeNode(n)
            index = inorder.index(n)
            root.left = dfs(preorder[1:index + 1], inorder[0:index])
            root.right = dfs(preorder[index + 1:], inorder[index + 1:])
            return root

        return dfs(preorder, inorder)

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = Solution().buildTree(preorder, inorder)
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.right.left.val)
print(root.right.right.val)

