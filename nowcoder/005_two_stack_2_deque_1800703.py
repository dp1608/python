# -*- coding: utf-8 -*-
# @Start_Time : 2018/7/3 15:46
# @End_time: 
# @Author  : Andy
# @Site    : 
# @File    : 005_two_stack_2_deque_1800703.py

"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if self.stack2:
            return self.stack2.pop()
        elif self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.pop()
        else:
            return None