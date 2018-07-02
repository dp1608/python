# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/2 11:21
# @End_time: 2018/7/2 11:32
# @Author  : Andy
# @Site    : 
# @File    : 112_path_sum_180702.py
"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum1):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        res = []
        if not root:
            return False

        def dfs(root, path):
            if not root.left and not root.right:
                path.append(root.val)
                res.append(sum(path))
                return
            if root.left:
                dfs(root.left, path + [root.val])
            if root.right:
                dfs(root.right, path + [root.val])

        dfs(root, [])
        # print(res)
        if sum1 in res:
            return True
        else:
            return False

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().hasPathSum(root, 12))
print(Solution().hasPathSum(root, 23))
