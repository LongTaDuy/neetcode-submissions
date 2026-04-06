class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum())        
        s = s.lower()
        if len(s) == 0:
            return True
        for i in range(int(len(s) / 2) + 1):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True