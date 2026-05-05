class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        lane1 = nums[0:len(nums)-1]
        lane2 = nums[1:len(nums)]

       
        def dfs(i,arr, memo):
            if i < 0:
                return 0
            if i == 0:
                return arr[0]
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(arr[i] + dfs(i - 2, arr, memo), dfs(i - 1, arr, memo))
                return memo[i]
        memo1 = {}
        memo2 = {}
        return max(dfs(len(lane1) - 1, lane1, memo1), dfs(len(lane2) - 1, lane2, memo2))

        
