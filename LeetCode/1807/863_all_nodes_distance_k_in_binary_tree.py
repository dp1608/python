# -*- coding: utf-8 -*-
# @StartTime : 2018/7/1 9:55
# @EndTime : 2018/7/1 9:55
# @Author  : Andy
# @Site    : 
# @File    : 863_all_nodes_distance_k_in_binary_tree.py
# @Software: PyCharm

"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
Output: [7,4,1]
Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.

Note:

The given tree is non-empty and has at most K nodes.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def distanceK(self, root, target, K):
        conn = collections.defaultdict(list)
        def connect(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)
        connect(None, root)
        bfs = [target.val]
        seen = set(bfs)
        for i in range(K):
            bfs = [y for x in bfs for y in conn[x] if y not in seen]
            seen |= set(bfs)
        return bfs


root = TreeNode(3)
root.left = TreeNode(5)
target = root.left
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

print(Solution().distanceK(root, target, 2))
    # def distanceK(self, root, target, K):
    #     """
    #     :type root: TreeNode
    #     :type target: TreeNode
    #     :type K: int
    #     :rtype: List[int]
    #     """
    #     if not root:
    #         return []
    #
    #     def find_K(k_val, root, dis):
    #         if not root:
    #             return None, None
    #         if root.val == k_val:
    #             return root, dis
    #         x, dis = find_K(k_val, root.left, dis + 1)
    #         y, dis = find_K(k_val, root.right, dis + 1)
    #         if x:
    #             return x,dis
    #         if y:
    #             return y,
    #
    #     tree, dis = find_K(target.val, root, 0)
    #     res = []
    #
    #     def find_in_tree(root, dis):
    #         if not root:
    #             return
    #         if dis == 0:
    #             res.append(root.val)
    #             return
    #         find_in_tree(root.left, dis - 1)
    #         find_in_tree(root.right, dis - 1)
    #
    #     find_in_tree(tree, K)



