class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen_nums:
                return [seen_nums[diff], i]
            else:
                seen_nums[nums[i]] = i
