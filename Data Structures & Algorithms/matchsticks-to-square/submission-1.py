class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        edge = sum(matchsticks) // 4
        edges = [0] * 4
        def backtrack(i):
            if i == len(matchsticks):
                return True
            for j in range(4):
                if matchsticks[i] + edges[j] > edge:
                    continue
                if j > 0 and edges[j] == edges[j - 1]:
                    continue
                edges[j] += matchsticks[i]
                if backtrack(i + 1):
                    return True
                edges[j] -= matchsticks[i]
            return False
        return backtrack(0)