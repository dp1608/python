# -*- coding: utf-8 -*-
# @StartTime : 2018/8/5 9:45
# @EndTime : 2018/8/5 9:45
# @Author  : Andy
# @Site    : 
# @File    : 885_boats_to_save_people_180805.py
# @Software: PyCharm


"""
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by
 a boat.)



Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
Note:

1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000
"""

#
# class Solution(object):
#     def numRescueBoats(self, people, limit):
#         """
#         :type people: List[int]
#         :type limit: int
#         :rtype: int
#         """
#         people.sort()
#         i = 0
#         res = 0
#         while i < len(people) - 1:
#             if people[i] + people[i + 1] <= limit:
#                 res += 1
#                 i += 2
#             else:
#                 break
#         res += len(people) - i
#         return res


# class Solution(object):
#     def numRescueBoats(self, people, limit):
#         """
#         :type people: List[int]
#         :type limit: int
#         :rtype: int
#         """
#         # people.sort()
#         dict_peo = {}
#         for i0 in range(len(people)):
#             if people[i0] in dict_peo:
#                 dict_peo[people[i0]] += 1
#             else:
#                 dict_peo[people[i0]] = 1
#
#
#         i = 0
#         res = 0
#         count = 0
#         while count < len(people):
#             # temp = people[i]
#             for key, value in dict_peo.items():
#                 if value < 1:
#                     dict_peo.pop(key)
#                     break
#                 temp = key
#                 minus = limit - temp
#                 index = 0
#                 dict_peo[key] -= 1
#                 for ii in range(minus, 0, -1):
#                     if ii in dict_peo:
#                         index = dict_peo[ii]
#                         if index < 1:
#                             continue
#                         dict_peo[ii] -= 1
#                         break
#
#                 if index > 0:
#                     count += 2
#                     res += 1
#                 else:
#                     res += 1
#                     count += 1
#                 if dict_peo[key] < 1:
#                     dict_peo.pop(key)
#                 break
#
#         return res


#
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        count = 0
        res = 0
        people.sort()
        index = 0
        for i in range(len(people) - 1, -1,-1):
            if i < index:
                break
            if people[i] == limit:
                res += 1
                count += 1
            else:
                if people[i] + people[index] <= limit:
                    count += 2
                    index += 1
                    res += 1
                else:
                    res += 1
                    count += 1

        return res


print(Solution().numRescueBoats([2,4], 5))
print(Solution().numRescueBoats([2,2], 6))
print(Solution().numRescueBoats([1,2], 3))
print(Solution().numRescueBoats([1,2,2,3], 3))