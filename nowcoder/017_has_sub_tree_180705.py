# -*- coding: utf-8 -*-
# @StartTime : 2018/7/4 10:10
# @EndTime : 2018/7/4 10:10
# @Author  : Andy
# @Site    : 
# @File    : 017_has_sub_tree_180704.py
# @Software: PyCharm
"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot2:
            return False
        if not pRoot1:
            return False
        if pRoot1.val == pRoot2.val:
            if self.compare(pRoot1, pRoot2):
                return True
        return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def compare(self, root1, root2):
        if not root2:
            return True
        if not root1:
            return False
        if root1.val != root2.val:
            return False
        if root1.val == root2.val:
            return self.compare(root1.right, root2.right) and self.compare(root1.left, root2.left)

a = TreeNode(1)
a.left = TreeNode(2)
b = TreeNode(2)
print(Solution().HasSubtree(a,b))