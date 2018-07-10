# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/10 11:10
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 024_find_path_in_tree_180710.py

"""
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        res = []

        def dfs(root, path):
            if not root:
                return
            if not root.left and not root.right:
                path.append(root.val)
                res.append(path)
                return
            if root.left:
                dfs(root.left, path+[root.val])
            if root.right:
                dfs(root.right, path + [root.val])

        dfs(root, [])
        # print(res)
        res_path = []
        for path in res:
            if sum(path) == expectNumber:
                res_path.append(path)
        return res_path


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(12)
root.left.left = TreeNode(4)
root.left.right = TreeNode(7)
res = Solution().FindPath(root,22)
print(res)