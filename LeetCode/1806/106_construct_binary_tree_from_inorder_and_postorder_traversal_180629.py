# -*- coding: utf-8 -*-
# @StartTime : 2018/6/29 11:05
# @EndTime : 2018/6/29 11:05
# @Author  : Andy
# @Site    : 
# @File    : 106_construct_binary_tree_from_inorder_and_postorder_traversal_180629.py
# @Software: PyCharm


"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return
        # root = TreeNode(preorder[0])

        def dfs(inorder, postorder):
            if not inorder:
                return None
            n = postorder[-1]
            root = TreeNode(n)
            index = inorder.index(n)
            root.left = dfs(inorder[0:index], postorder[0:index])
            root.right = dfs(inorder[index + 1:], postorder[index:-1])
            return root
        return dfs(inorder, postorder)



inorder = [9, 3, 15, 20, 7]
postorder = [9,15,7,20,3]
root = Solution().buildTree(inorder, postorder)
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.right.left.val)
print(root.right.right.val)
