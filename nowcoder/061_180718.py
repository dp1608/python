# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/18 14:25
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 061_180718.py

"""
请实现两个函数，分别用来序列化和反序列化二叉树
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        # write code here
        s = []
        def preorder(root):
            if not root:
                s.append("#")
                return
            s.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return s


    def Deserialize(self, s):
        # write code here
        def core(s):
            if not s:
                return None
            if s[0] == "#":
                del s[0]
                return None
            root = TreeNode(s[0])
            del s[0]
            root.left = core(s)
            root.right = core(s)
            return root

        return core(s)
