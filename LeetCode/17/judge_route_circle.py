# -*- coding: utf-8 -*-
# @StartTime : 9/21/2017 21:26
# @EndTime   : 9/21/2017 21:58
# @Author    : Andy
# @Site      : 
# @File      : judge_route_circle.py
# @Software  : PyCharm

"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves,
    judge if this robot makes a circle, which means it moves back to the original place.
The move sequence is represented by a string. And each move is represent by a character.
The valid robot moves are R (Right), L (Left), U (Up) and D (down).
The output should be true or false representing whether the robot makes a circle.
Example 1:
    Input: "UD"
    Output: true
Example 2:
    Input: "LL"
    Output: false
"""


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        step=[0,0]
        for i in range(0,len(moves)):
            if moves[i] == 'L':
                step[0] = step[0]+1
            if moves[i] == 'R':
                step[0] = step[0]-1
            if moves[i] == 'U':
                step[1] = step[1]+1
            if moves[i] == 'D':
                step[1] = step[1]-1

        if step[0] == 0 and step[1] == 0:
            return True
        else:
            return False


a=Solution()
print a.judgeCircle('UDD')

