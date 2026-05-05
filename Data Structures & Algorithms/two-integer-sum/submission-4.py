class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement not in seen_nums:
                seen_nums[n] = i
            else:
                return [seen_nums[complement],i]
            #seen_nums[n] = i