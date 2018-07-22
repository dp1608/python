# -*- coding: utf-8 -*-
# @StartTime : 2018/7/22 9:33
# @EndTime : 2018/7/22 9:33
# @Author  : Andy
# @Site    : 
# @File    : 872_leaf_similar_trees_180722.py
# @Software: PyCharm


"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value
sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 or not root2:
            return root1 == root2


        def dfs(root, res):
            if root.left:
                dfs(root.left, res)
            if root.right:
                dfs(root.right, res)
            if not root.left and not root.right:
                res.append(root.val)
            return res
        leaf1 = dfs(root1, [])
        leaf2 = dfs(root2, [])

        if leaf1[:] == leaf2[:]:
            return True
        else:
            return False



        # tree1 = [root1]
        # leaf1 = []
        # tree2 = [root2]
        # leaf2 = []
        #
        # while tree1:
        #     this = tree1[0]
        #     del tree1[0]
        #     if this.left:
        #         tree1.append(this.left)
        #     if this.right:
        #         tree1.append(this.right)
        #     if not this.right and not this.left:
        #         leaf1.append([this.val])
        #
        # while tree2:
        #     this = tree2[0]
        #     del tree2[0]
        #     if this.left:
        #         tree2.append(this.left)
        #     if this.right:
        #         tree2.append(this.right)
        #     if not this.right and not this.left:
        #         leaf2.append([this.val])
        #


root = TreeNode(1)
root2 = TreeNode(1)
print(Solution().leafSimilar(root, root2))
a = [1,2,3,4]
b = [1,2,3,4]
print([1,2,3,4] == [1,2,3,4])
print(a[:] == b[:])


