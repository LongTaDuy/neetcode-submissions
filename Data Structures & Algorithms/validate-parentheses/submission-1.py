class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i in range(len(s)):
            if s[i] in d:
                if len(stack) != 0 and d[s[i]] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if len(stack) == 0:
            return True
        return False
