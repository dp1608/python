# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/13 16:36
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 039_balanced_tree_180713.py
"""
判断是否为平衡二叉树
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            if left == -1:
                return -1
            right = dfs(root.right)
            if right == -1:
                return -1
            if left - right > 1 or left - right < -1:
                return -1
            else:
                return max(left, right) + 1

        if dfs(pRoot) == -1:
            return False
        else:
            return True


