# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/13 16:29
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 038_tree_depth_180713.py

"""
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        # write code here

        def dfs(root):
            if not root:
                return 0
            else:
                return max(dfs(root.left) + 1, dfs(root.right) + 1)
        return dfs(pRoot)