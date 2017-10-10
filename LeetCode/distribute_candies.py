# -*- coding: utf-8 -*-
# @StartTime : 9/27/2017 23:10
# @EndTime   : 9/27/2017 23:33
# @Author    : Andy
# @Site      : 
# @File      : distribute_candies.py
# @Software  : PyCharm


"""
    Given an integer array with even length, where different numbers in this array represent
different kinds of candies. Each number means one candy of the corresponding kind. You need to
distribute these candies equally in number to brother and sister. Return the
maximum number of kinds of candies the sister could gain.
Example 1:
    Input: candies = [1,1,2,2,3,3]
    Output: 3
Explanation:
    There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
    Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
    The sister has three different kinds of candies.
Example 2:
    Input: candies = [1,1,2,3]
    Output: 2
Explanation:
    For example, the sister has candies [2,3] and the brother has candies [1,1].
    The sister has two different kinds of candies, the brother has only one kind of candies.
Note:
The length of the given array is in range [2, 10,000], and will be even.
The number in given array is in range [-100,000, 100,000].
"""


class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        len_list = len(candies)
        sister_candies_number = len_list/2
        kinds_of_candies = len(list(set(candies)))
        if sister_candies_number <= kinds_of_candies:
            return sister_candies_number
        else:
            return kinds_of_candies


Distri = Solution()
candies = [1,1,2,3,4,5]
result=Distri.distributeCandies(candies)
print result
