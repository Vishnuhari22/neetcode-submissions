class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        freqMap = {}
        added = set()
        size = len(nums) // 3
        for num in nums:
            freqMap[num] = freqMap.get(num,0) + 1
        
        for num in nums:
            if freqMap[num] > size and num not in added:
                result.append(num)
                added.add(num)

        return result

