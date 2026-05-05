class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i, j = 0, 0
        while i < min(len(word1),len(word2)):
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1

        if len(word2) > len(word1):
            res += word2[j:]
        else:
            res += word1[i:]

        return res