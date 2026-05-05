class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency = set()
        for i in nums:
            frequency.add(i)
        if len(nums) != len(frequency):
            return True
        return False