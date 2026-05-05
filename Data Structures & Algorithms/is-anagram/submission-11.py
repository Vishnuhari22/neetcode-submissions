class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        for i in s:
            freq[i] = freq.get(i, 0) + 1
        for j in t:
            freq[j] = freq.get(j, 0) - 1

        for k in freq:
            if freq[k] == 0:
                continue
            else:
                return False
        return True