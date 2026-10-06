class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        min_heap = [(0, k)] # (w, v)
        t = 0
        visited = set()
        while min_heap:
            w1, v1 = heapq.heappop(min_heap)
            if v1 in visited:
                continue
            visited.add(v1)
            t = max(w1, t)
            for v2, w2 in edges[v1]:
                heapq.heappush(min_heap, (w1 + w2, v2))
        return t if len(visited) == n else -1
            