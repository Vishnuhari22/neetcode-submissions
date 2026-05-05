class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def choice(i):
            if i < 0:
                return 0
            if i == 0:
                return nums[i]

            if i in memo:
                return memo[i]
            else:
                memo[i] = max(nums[i] + choice(i - 2), choice(i - 1))
                return memo[i]

        return choice(len(nums) - 1)
            
