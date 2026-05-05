class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start_index, current_combination, remaining_val):
            if remaining_val == 0:
                result.append(current_combination[:])
                return
            if remaining_val < 0:
                return
            for i in range(start_index, len(nums)):
                if nums[i] > target:
                    continue
                current_combination.append(nums[i])
                backtrack(i, current_combination, remaining_val - nums[i])
                current_combination.pop()
        backtrack(0, [], target)
        return result
                
            