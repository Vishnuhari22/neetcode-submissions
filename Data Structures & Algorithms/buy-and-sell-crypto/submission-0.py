class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        n = len(prices)
        max_profit = 0

        for r in range(1,n):
            while prices[l] > prices[r]:
                l += 1
            cur_profit = prices[r] - prices[l]
            max_profit = max(cur_profit,max_profit)

        return max_profit