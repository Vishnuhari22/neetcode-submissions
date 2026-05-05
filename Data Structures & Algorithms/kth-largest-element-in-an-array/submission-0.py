class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_New = [-i for i in nums]
        heapq.heapify(nums_New)

        
        while k > 0:
            res = heapq.heappop(nums_New)
            k -= 1

        return -res
