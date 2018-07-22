# -*- coding: utf-8 -*-
# @StartTime : 2018/7/22 9:49
# @EndTime : 2018/7/22 9:49
# @Author  : Andy
# @Site    : 
# @File    : 874_walking_robot_simulation_180722.py
# @Software: PyCharm

"""
A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types
 of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles.

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues
following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.



Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)


Note:

0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
The answer is guaranteed to be less than 2 ^ 31.
"""
# class Solution:
#     def robotSim(self, commands, obstacles):
#         i = j = mx = d = 0
#         move, obstacles = [(0, 1), (1, 0), (0, -1), (-1, 0)], set(map(tuple, obstacles))
#         for command in commands:
#             if command == -1:
#                 d = (d + 1) % 4
#             elif command == -2:
#                 d = (d - 1) % 4
#             else:
#                 x, y = move[d]
#                 while command and (i + x, j + y) not in obstacles:
#                     i += x
#                     j += y
#                     command -= 1
#             mx = max(mx, i ** 2 + j ** 2)
#         return mx

class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        x = 0
        y = 0
        forward = 0
        obs_x = {}
        obs_y = {}
        res = 0

        for ii in range(len(obstacles)):
            temp = obstacles[ii]
            if temp[0] not in obs_x.keys():
                obs_x[temp[0]] = set([temp[1]])
            else:
                obs_x[temp[0]].add(temp[1])

            if temp[1] not in obs_y.keys():
                obs_y[temp[1]] = set([temp[0]])
            else:
                obs_y[temp[1]].add(temp[0])

        # print(obs_x)
        # print(obs_y)

        def obs(x, y, x2, y2, forward):
            if forward == 0:
                if x in obs_x.keys():
                    temp = obs_x[x]
                    for ll in temp:
                        if y < ll and y2 >= ll:
                            y2 = ll - 1
            if forward == 2:
                if x in obs_x.keys():
                    temp = obs_x[x]
                    for ll in temp:
                        if y > ll and y2 <= ll:
                            y2 = ll + 1

            if forward == 1:
                if y in obs_y.keys():
                    temp = obs_y[y]
                    for ll in temp:
                        if x < ll and x2 >= ll:
                            x2 = ll - 1

            if forward == 3:
                if y in obs_y.keys():
                    temp = obs_y[y]
                    for ll in temp:
                        if x > ll and x2 <= ll:
                            x2 = ll + 1
            return x2, y2

        def dfs(x, y, forward, go):
            if forward == 0:
                x, y = obs(x, y, x, y + go, forward)
            if forward == 1:
                x, y = obs(x, y, x + go, y, forward)
            if forward == 2:
                x, y = obs(x, y, x, y - go, forward)
            if forward == 3:
                x, y = obs(x, y, x - go, y, forward)
            return x, y

        for i in commands:
            if i == -1:
                forward += 1
                forward %= 4
            elif i == -2:
                forward -= 1
                forward %= 4
            else:
                x, y = dfs(x, y, forward, i)
                if res < x * x + y * y:
                    res = x * x + y * y

        return res


print(Solution().robotSim([4,-1,3], []))
print(Solution().robotSim([4,-1,4,-2,4],  [[2,4]]))