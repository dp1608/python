# -*- coding: utf-8 -*-
# @StartTime : 2018/7/17 22:48
# @EndTime : 2018/7/17 22:48
# @Author  : Andy
# @Site    : 
# @File    : 059_180717.py
# @Software: PyCharm

"""
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        deque = [pRoot]
        reverse = False
        res = []

        while deque:
            count = len(deque)
            next_deque = []
            temp = []
            if not reverse:
                for _ in range(count):
                    this = deque.pop()
                    if this.left:
                        next_deque.append(this.left)
                    if this.right:
                        next_deque.append(this.right)
                    temp.append(this.val)
                deque = next_deque[:]
                res.append(temp)
                reverse = ~reverse
            else:
                for _ in range(count):
                    this = deque.pop()
                    if this.right:
                        next_deque.append(this.right)
                    if this.left:
                        next_deque.append(this.left)
                    temp.append(this.val)
                    # del deque[0]
                deque = next_deque[:]
                res.append(temp)
                reverse = ~reverse

        return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.right = TreeNode(5)
# root.right = TreeNode(6)
root.right.right = TreeNode(7)
print(Solution().Print(root))