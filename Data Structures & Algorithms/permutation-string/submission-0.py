class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        check = [0] * 26
        for i in s1:
            check[ord(i) - ord('a')] += 1
        left = 0
        right = length
        while right <= len(s2):
            ans = [0] * 26
            for i in s2[left:right]:
                ans[ord(i) - ord('a')] += 1
            if ans == check:
                return True
            left += 1
            right += 1
        return False

