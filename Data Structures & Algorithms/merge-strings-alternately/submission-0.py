class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1:
            return word2
        if not word2:
            return word1
        check1 = 0
        check2 = 0
        res = ""
        while check1 < len(word1) and check2 < len(word2):
            res =  res + word1[check1]
            check1 += 1
            res = res + word2[check2]
            check2 += 1
        if check1 < len(word1):
            res += word1[check1:]
        if check2 < len(word2):
            res += word2[check2:]
        return res