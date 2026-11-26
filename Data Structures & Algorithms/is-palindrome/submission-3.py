class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and self.check(s[l]) == False:
                l += 1
            while l < r and self.check(s[r]) == False:
                r -= 1
            if s[r].lower() != s[l].lower():
                return False
            r -= 1
            l += 1
        return True
        
    def check(self, c):
        if ord(c) >= ord('A') and ord(c) <= ord('Z'):
            return True
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            return True
        if ord(c) >= ord('0') and ord(c) <= ord('9'):
            return True
        return False
