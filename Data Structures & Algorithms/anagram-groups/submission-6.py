class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            s_key = "".join(sorted(s))
            if s_key not in groups:
                groups[s_key] = [s]
            else:
                groups[s_key].append(s)

        return list(groups.values())