class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        numsSet = set()
        for num in nums:
            numsSet.add(num)

        return len(nums) != len(numsSet)
        