class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        curSum = 0
        res = float('inf')
        for R in range(len(nums)):
            curSum += nums[R]
            while curSum >= target:
                res = min(R - L + 1, res)
                curSum -= nums[L]
                L += 1
        return res if res != float('inf') else 0 