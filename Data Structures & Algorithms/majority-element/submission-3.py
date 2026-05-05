class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqMap = {}
        for i in nums:
            freqMap[i] = freqMap.get(i,0) + 1
        return max(freqMap, key = freqMap.get)