class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('INF')] * n
        dist[k - 1] = 0
        for _ in range(n - 1):
            for u, v, w in times:
                if dist[u - 1] != float('INF') and dist[u - 1] + w < dist[v - 1]:
                    dist[v - 1] = dist[u - 1] + w
        return max(dist) if max(dist) < float('INF') else -1

