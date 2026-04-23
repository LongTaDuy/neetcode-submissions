class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, countT = {}, {}
        if t == "":
            return ""

        # tao freq map cho t
        for i in t:
            countT[i] = 1 + countT.get(i, 0)
        have, need = 0, len(countT)
        min_count = float('infinity')
        left = 0
        res = [-1, -1]
        for right in range(len(s)):
            window[s[right]] = 1 + window.get(s[right], 0)
            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have += 1
            while have == need:
                if right - left + 1 < min_count:
                    res = [left, right]
                    min_count = right - left + 1
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left, right = res
        return s[left : right + 1] if min_count != float("infinity") else ""
