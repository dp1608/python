# -*- coding: utf-8 -*-
# @StartTime : 2018/7/9 22:19
# @EndTime : 2018/7/9 22:19
# @Author  : Andy
# @Site    : 
# @File    : 020_baohan_min_stack_180709.py
# @Software: PyCharm

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.assist = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        min_pre = self.min()
        if not min_pre:
            self.assist.append(node)
        else:
            self.assist.append(min(node,min_pre))

    def pop(self):
        # write code here
        if self.stack:
            self.assist.pop()
            return self.stack.pop()

    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def min(self):
        # write code here
        if self.assist:
            return self.assist[-1]
        else:
            return None