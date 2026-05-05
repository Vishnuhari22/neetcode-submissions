class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0
        n = len(prices)
        for r in range(1,n):
            while prices[r] - prices[l] < 0:
                l += 1
            maxP = max(maxP, prices[r] - prices[l])
        return maxP
