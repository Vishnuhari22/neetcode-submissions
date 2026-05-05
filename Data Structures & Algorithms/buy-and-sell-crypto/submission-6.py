class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        L = 0
        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            cur_profit = prices[R] - prices[L]
            max_profit = max(max_profit, cur_profit)
        return max_profit