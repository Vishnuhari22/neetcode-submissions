class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = max(nums)
        
        for i in range(len(nums)):
            p = nums[i]
            j = i + 1
            while j < len(nums):
                p = p * nums[j]
                max_p = max(max_p, p)
                j += 1
        return max_p