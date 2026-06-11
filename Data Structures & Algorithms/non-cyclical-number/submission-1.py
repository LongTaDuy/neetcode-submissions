import math
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumsquare(n)
        if n == 1:
            return True
        return False
    def sumsquare(self, n):
        sum = 0
        while n:
            sum += (n % 10) ** 2
            n = n // 10
        return sum




