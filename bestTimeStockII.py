class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if n <2:
            return 0
        profit = 0
        for i in range(n-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1]-prices[i]
        return profit
