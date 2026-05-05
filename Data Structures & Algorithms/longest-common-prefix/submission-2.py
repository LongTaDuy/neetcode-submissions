class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        res = ""
        strs.sort()
        for i in range(len(strs[0])):
            cnt = 0
            for j in range(len(strs) - 1):
                if strs[j][i] == strs[j + 1][i]:
                    cnt += 1
                else:
                    return res
                if cnt == len(strs) - 1:
                    res = res + strs[j][i]
        return res