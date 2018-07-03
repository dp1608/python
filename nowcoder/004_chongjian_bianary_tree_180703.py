# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/3 15:38
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 004_chongjian_bianary_tree_180703.py
"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre:
            return None
        root = TreeNode(pre[0])
        index = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:index + 1], tin[0:index])
        root.right = self.reConstructBinaryTree(pre[index + 1:], tin[index + 1:])
        return root


