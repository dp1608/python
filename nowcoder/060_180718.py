# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/18 10:15
# @End_time: 2018/7/18 10:22
# @Author  : Andy
# @Site    : 
# @File    : 060_180718.py

"""
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        deque = [pRoot]
        while deque:
            count = len(deque)
            temp = []
            for _ in range(count):
                tree = deque[0]
                deque = deque[1:]
                if tree.left:
                    deque.append(tree.left)
                if tree.right:
                    deque.append(tree.right)
                temp.append(tree.val)
            res.append(temp)
        return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.right = TreeNode(5)
# root.right = TreeNode(6)
root.right.right = TreeNode(7)
print(Solution().Print(root))