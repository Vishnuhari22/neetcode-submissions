class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window = set()
        L = 0
        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            longest = max(R - L + 1, longest)
            window.add(s[R])
        return longest 