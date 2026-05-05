class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        maxP = 0
        curP = 0
        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            curP = prices[R] - prices[L]
            maxP = max(curP,maxP)
        return maxP