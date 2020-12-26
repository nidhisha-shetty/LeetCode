# Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

#Solution
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        min_price=sys.maxint
        for x in range(len(prices)):
            if prices[x]<min_price:
                min_price=prices[x]
            elif (prices[x]-min_price)>max_profit:
                max_profit=prices[x]-min_price
                
        return max_profit
