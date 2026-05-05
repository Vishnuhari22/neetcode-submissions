class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            M = (L + R)//2
            if nums[M] == target:
                return M
            elif target > nums[M]:
                L = M + 1
            else:
                R = M - 1
        return L