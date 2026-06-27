class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = {}
        freqT = {}

        for i in range(len(s)):
            freqS[s[i]] = freqS.get(s[i], 0) + 1
        for j in range(len(t)):
            freqT[t[j]] = freqT.get(t[j], 0) + 1

        return freqS == freqT
