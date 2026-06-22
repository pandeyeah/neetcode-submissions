class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        profit=0
        j=1
        for i in range(j,len(prices)):
            margin=prices[i]-buy
            profit=max(margin,profit)
            if prices[i]<buy: buy=prices[i]
        return profit