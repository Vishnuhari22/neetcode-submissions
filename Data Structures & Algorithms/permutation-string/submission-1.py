class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqS1 = {}
        freqS2 = {}
        l = 0
        freq_window = {}

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            freqS1[s1[i]] = freqS1.get(s1[i],0) + 1

        for r in range(len(s2)):
            while (r - l) + 1 > len(s1):
                freq_window[s2[l]] -= 1
                if freq_window[s2[l]] ==0:
                    del freq_window[s2[l]]
                l += 1
            
            freq_window[s2[r]] = freq_window.get(s2[r],0) + 1
            

            if freq_window == freqS1:
                return True
        return False

        

        