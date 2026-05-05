class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqS1 = {}
        freqS2 = {}
        L = 0

        for i in range(len(s1)):
            freqS1[s1[i]] = freqS1.get(s1[i], 0) + 1

        for R in range(len(s2)):
            while R - L + 1 > len(s1):
                freqS2[s2[L]] -= 1
                if freqS2[s2[L]] == 0:
                    del freqS2[s2[L]]
                L += 1

            freqS2[s2[R]] = freqS2.get(s2[R], 0) + 1

            if freqS1 == freqS2:
                return True
        return False
