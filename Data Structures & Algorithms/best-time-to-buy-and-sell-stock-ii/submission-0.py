class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        n = len(prices)
        totalProfit = 0
        for r in range(1,n):
            if prices[r] < prices[l]:
                l = r
            else:
                totalProfit += prices[r] - prices[l]
                l = r
        return totalProfit