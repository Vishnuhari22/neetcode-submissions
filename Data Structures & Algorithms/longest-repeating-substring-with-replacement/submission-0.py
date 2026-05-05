class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        longest = 0
        
        for r in range(len(s)):
            
            freq[s[r]] = freq.get(s[r], 0) + 1
            
            
            max_freq = max(freq.values())
            
            window_size = (r - l) + 1
            
            
            while window_size - max_freq > k:
                freq[s[l]] -= 1
                l += 1
                window_size = (r - l) + 1  
            
            longest = max(longest, window_size)
        
        return longest