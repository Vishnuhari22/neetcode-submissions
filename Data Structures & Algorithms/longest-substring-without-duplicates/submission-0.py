class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        longest = 0
        sett = set()

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            cur_sum = (r - l) + 1
            longest = max(longest, cur_sum)
            sett.add(s[r])

        return longest