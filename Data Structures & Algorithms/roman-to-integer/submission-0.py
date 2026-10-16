class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if s[i] == 'I':
                if i + 1 < len(s) and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                    res -= 1
                else:
                    res += 1
            elif s[i] == 'X':
                if i + 1 < len(s) and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                    res -= 10
                else:
                    res += 10
            elif s[i] == 'C':
                if i + 1 < len(s) and (s[i + 1] == 'M' or s[i + 1] == 'D'):
                    res -= 100
                else:
                    res += 100
            else:
                res += roman[s[i]]
        return res
