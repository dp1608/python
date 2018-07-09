# -*- coding: utf-8 -*-
# @StartTime : 2018/7/9 18:40
# @EndTime : 2018/7/9 18:40
# @Author  : Andy
# @Site    : 
# @File    : 018_mirror_tree_180709.py
# @Software: PyCharm

"""
操作给定的二叉树，将其变换为源二叉树的镜像。
输入描述:
二叉树的镜像定义：源二叉树
             8
           /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return root

        def dfs(root):
            if not root:
                return None
            temp = root.right
            root.right = dfs(root.left)
            root.left = dfs(temp)
            return root

        return dfs(root)


a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
root = Solution().Mirror(a)
print(root.val)
print(root.left.val)
print(root.right.val)
















