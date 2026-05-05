class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        cur_len = 0
        longest = 0
        L = 0

        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
            cur_len = R - L + 1

            longest = max(longest, cur_len)
        return longest
