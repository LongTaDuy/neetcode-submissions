class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                leftskip = s[left + 1 : right + 1]
                rightskip = s[left : right]
                return leftskip == leftskip[::-1] or rightskip == rightskip[::-1]
            left += 1
            right -= 1
        return True
 