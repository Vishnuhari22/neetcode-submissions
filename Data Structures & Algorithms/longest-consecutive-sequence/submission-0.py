class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for i in num_set:
            if (i-1) not in num_set:
                cur_num = i
                cur_len = 1
                while (cur_num + 1) in num_set:
                    cur_num += 1
                    cur_len += 1
                max_len = max(cur_len,max_len)
        return max_len
            
