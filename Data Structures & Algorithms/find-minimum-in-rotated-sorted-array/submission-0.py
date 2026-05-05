class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        min_value = min(nums[l],nums[r])
        while l <= r:
            mid = (l+r)//2
            min_value = min(min_value,nums[mid])
            if nums[mid] > min_value:
                l = mid + 1
            else:
                r = mid - 1
        return min_value