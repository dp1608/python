# -*- coding: utf-8 -*-
# @StartTime : 2018/7/17 22:20
# @EndTime : 2018/7/17 22:20
# @Author  : Andy
# @Site    : 
# @File    : 058_180717.py
# @Software: PyCharm

"""
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        in_1 = []
        in_0 = []
        in_2 = []
        in_3 = []

        def inorder(root):
            if not root:
                in_1.append('#')
                return
            inorder(root.left)
            in_1.append(root.val)
            inorder(root.right)

        def preorder(root):
            if not root:
                in_0.append('#')
                return

            in_0.append(root.val)
            preorder(root.left)
            preorder(root.right)

        def reverse_inorder(root):
            if not root:
                in_2.append('#')
                return
            reverse_inorder(root.right)
            in_2.append(root.val)
            reverse_inorder(root.left)

        def reverse_preorder(root):
            if not root:
                in_3.append('#')
                return
            in_3.append(root.val)
            reverse_preorder(root.right)

            reverse_preorder(root.left)


        inorder(pRoot)
        reverse_inorder(pRoot)

        preorder(pRoot)
        reverse_preorder(pRoot)
        print(in_1)
        print(in_2)
        if in_1[:] == in_2[:] and in_0[:] == in_3[:]:
            return True
        else:
            return False


root = TreeNode(5)
root.left = TreeNode(5)
root.right = TreeNode(5)
root.left.left = TreeNode(5)
root.left.left.right = TreeNode(5)
root.right = TreeNode(5)
root.right.right = TreeNode(5)

print(Solution().isSymmetrical(root))

