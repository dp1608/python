# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/10 15:46
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 026_proot_of_tree_180710.py

"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。

"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        tree_list = []
        if not pRootOfTree:
            return None

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            tree_list.append(root)
            dfs(root.right)

        dfs(pRootOfTree)
        for i in range(len(tree_list)):
            if i == 0:
                tree_list[i].left = None
                if len(tree_list) > 1:
                    tree_list[i].right = tree_list[i + 1]
                continue
            if i == len(tree_list) - 1:
                tree_list[i].right = None
                tree_list[i].left = tree_list[i - 1]
                continue
            tree_list[i].right = tree_list[i + 1]
            tree_list[i].left = tree_list[i - 1]
        return tree_list[0]
