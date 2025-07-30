# Last updated: 7/30/2025, 12:24:50 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0]
        profit = 0
        for i in prices :
            mi = min(i,mi)
            profit = max(profit,i-mi)
        return profit
        