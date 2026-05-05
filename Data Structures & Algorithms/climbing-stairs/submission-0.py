class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0:1, 1:1}

        def climb(n):
            if n <= 1:
                return 1
            if n in memo:
                return memo[n]
            else:
                memo[n] = climb(n - 1) + climb(n - 2)
                return memo[n]

        return climb(n)
        