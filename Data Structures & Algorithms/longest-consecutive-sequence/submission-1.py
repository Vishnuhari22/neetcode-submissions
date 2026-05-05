class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSeq = 0
        curSeq = 0
        unique = set(nums)

        for num in unique:
            if num - 1 not in unique:
                curSeq = 1
                while num + curSeq in unique:
                    curSeq += 1
                maxSeq = max(maxSeq,curSeq)
        return maxSeq