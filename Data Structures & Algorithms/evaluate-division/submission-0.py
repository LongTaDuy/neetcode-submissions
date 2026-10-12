class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])
        def bfs(src, dst):
            if src not in adj or dst not in adj:
                return -1
            q, visited = deque(), set()
            q.append([src, 1])
            visited.add(src)
            while q:
                node, w = q.popleft()
                if node == dst:
                    return w
                visited.add(node)
                for nei, weight in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append([nei, w * weight])
            return -1

        return [bfs(a, b) for a, b in queries]
