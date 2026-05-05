class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        L = 0
        longest = 0

        for R in range(len(s)):
            freq[s[R]] = freq.get(s[R], 0) + 1

            max_freq = max(freq.values())

            window_size = R - L + 1

            while window_size - max_freq > k:
                freq[s[L]] -= 1
                L += 1
                window_size = R - L + 1
            
            longest = max(longest, window_size)

        return longest