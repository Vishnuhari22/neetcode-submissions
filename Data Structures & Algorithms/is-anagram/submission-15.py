class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqS = {}
        for i in range(len(s)):
            freqS[s[i]] = freqS.get(s[i], 0) + 1
        freqT = {}
        for j in range(len(t)):
            freqT[t[j]] = freqT.get(t[j], 0) + 1
        
        return freqS == freqT
