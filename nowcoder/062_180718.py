# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/18 10:23
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 062_180718.py

"""
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）
  中，按结点数值大小顺序第三小结点的值为4。

"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        res_in = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res_in.append(root)
            inorder(root.right)

        inorder(pRoot)
        if k > len(res_in) or k < 1:
            return None
        return res_in[k - 1]
