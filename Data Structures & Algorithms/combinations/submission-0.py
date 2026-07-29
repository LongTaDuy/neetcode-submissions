class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, sub):
            if len(sub) == k:
                res.append(sub.copy())
                return
            for i in range(start, n + 1):
                sub.append(i)
                backtrack(i + 1, sub)
                sub.pop()
        backtrack(1, [])
        return res