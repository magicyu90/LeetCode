# coding:utf-8
class Solution:
    """
    Say you have an array for which the ith element is the price of a given stock on day i.
    Design an algorithm to find the maximum profit. 
    You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
    However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    """

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        size = len(prices)
        if size <= 1:
            return 0
        for i in range(size - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]

        return profit


solution = Solution()
print(solution.maxProfit([4, 7, 8, 2, 8]))
