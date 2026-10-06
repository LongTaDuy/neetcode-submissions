class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w)) # (dst, cost)
        min_heap = [(0, -1, src)] #cost, stop, node
        dist = [[float("inf")]* (k + 5) for i in range(n)]
        while min_heap:
            cost, stop, node = heapq.heappop(min_heap)
            if node == dst:
                return cost
            if stop >= k or dist[node][stop + 1] < cost:
                continue
            for nei, c in adj[node]:
                new_cost = cost + c
                new_stop = stop + 1
                if new_cost < dist[nei][new_stop + 1]:
                    dist[nei][new_stop + 1] = new_cost
                    heapq.heappush(min_heap, (new_cost, new_stop, nei))
        return -1
