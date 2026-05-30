class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        q = deque([(0, -1)]) # store the current node and its parent
        visit.add(0)
        while q:
            node, parent = q.popleft()
            # check it has cycle
            for nei in adj[node]:
                # avoid it adj to its parent 
                if nei == parent:
                    continue
                # check it has cycle

                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, node))
        return len(visit) == n
            