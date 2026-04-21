class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check1 = [0] * 26
        check2 = [0] * 26
        length = len(s1)
        for i in s1:
            check1[ord(i) - ord('a')] += 1
        left = 0
        right = length
        for i in s2[left : right]:
            check2[ord(i) - ord('a')] += 1
        if check1 == check2:
            return True
        for right in range(length, len(s2)):
            check2[ord(s2[right]) - ord('a')] += 1
            check2[ord(s2[left]) - ord('a')] -= 1
            if check1 == check2:
                return True
            left += 1
            right += 1
        return False