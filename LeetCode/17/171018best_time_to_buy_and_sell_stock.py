# -*- coding: utf-8 -*-
# @StartTime : 10/18/2017 15:13
# @EndTime   : 10/18/2017 15:58
# @Author    : Andy
# @Site      : 
# @File      : 171018best_time_to_buy_and_sell_stock.py
# @Software  : PyCharm

"""
Say you have an array for which the ith element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be
larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        max_profit = 0
        min_price = prices[0]
        for num in prices:
            min_price = min(min_price, num)
            if num - min_price > max_profit:
                max_profit = num - min_price
            # max_profit = max(num - min_price, max_profit)
        return max_profit



# Wrong answer of [7,2,4,1]
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if len(prices) == 0:
#             return 0
#         max_price = max(prices)
#         min_price = min(prices)
#         max_index = prices.index(max_price)
#         min_index = prices.index(min_price)
#         return max(max_price - min(prices[0:max_index + 1]),
#                    max(prices[min_index:]) - min_price)

So = Solution()
print So.maxProfit([7, 1, 5, 3, 6, 4])
print So.maxProfit([7, 6, 4, 3, 1])
print So.maxProfit([7, 2, 4, 1])
print So.maxProfit([])
