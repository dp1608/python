# -*- coding: utf-8 -*-
# @StartTime : 2018/6/30 9:22
# @EndTime : 2018/6/30 9:22
# @Author  : Andy
# @Site    : 
# @File    : 671_second_minimum_node_in_a_binary_tree_180630.py
# @Software: PyCharm

"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input:
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root.left:
            return -1
        minimum = root.val
        sec_mini = 0
        tree = [root.left, root.right]
        while tree:
            temp = tree[0]
            if temp.val > minimum and (sec_mini == 0 or temp.val < sec_mini) :
                sec_mini = temp.val
                # return sec_mini
            if temp.left:
                tree.append(temp.left)
                tree.append(temp.right)
            del tree[0]
        if not sec_mini:
            return -1
        return sec_mini


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
print(Solution().findSecondMinimumValue(root))

