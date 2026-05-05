class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_val = min(nums[l],nums[r])
        while l <= r:
            m = l + (r - l) // 2
            min_val = min(min_val,nums[m])
            if nums[m] > min_val:
                l = m + 1
            else:
                r = m - 1
        return min_val
