class Solution:
    def isValid(self, s: str) -> bool:
        check_map = {"(":")","{":"}","[":"]"}
        stack = []
        
        for char in s:
            if char in check_map:
                stack.append(char)
                
            else:
                if len(stack) == 0:
                    return False
                if char  != check_map[stack[-1]]:
                    return False
                stack.pop()

        return len(stack) == 0