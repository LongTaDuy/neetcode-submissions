class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        def isdivisor(l):
            if len1 % l != 0 or len2 % l != 0:
                return False
            l1, l2 = len1 // l, len2 // l
            return l1 * str1[:l] == str1 and l2 * str1[:l] == str2

        
        for l in range(min(len1, len2), 0, -1):
            if isdivisor(l):
                return str1[:l]
        return ""