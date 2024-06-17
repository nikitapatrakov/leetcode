class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        min_len = min([len(s) for s in strs])
        for i in range(min_len):
            current = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != current:
                    return strs[0][:i]
        return strs[0][:min_len]