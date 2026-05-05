class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqS = {}
        freqT = {}

        for i in s:
            if i not in freqS:
                freqS[i] = 1
            else:
                freqS[i] += 1
        
        for j in t:
            if j not in freqT:
                freqT[j] = 1
            else:
                freqT[j] += 1
        
        if freqS != freqT:
            return False
        return True
