class Solution:
    def decodeString(self, s: str) -> str:
        stringstack = []
        countstack = []
        k = 0
        cur = ""
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                stringstack.append(cur)
                countstack.append(k)
                k = 0
                cur = ""
            elif c == "]":
                temp = cur
                cur = stringstack.pop()
                cnt = countstack.pop()
                cur += temp * cnt
            else:
                cur += c
        return cur