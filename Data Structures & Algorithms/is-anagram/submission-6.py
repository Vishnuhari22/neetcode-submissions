class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqS = {}
        freqT = {}

        for i in s:
            freqS[i] = freqS.get(i,0) + 1
        
        for j in t:
            freqT[j] = freqT.get(j,0) + 1
        
        if freqS != freqT:
            return False
        return True
