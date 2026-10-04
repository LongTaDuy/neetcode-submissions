class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N + 1)]
        rank = [1] * (N + 1)
        def find(n):
            if n == par[n]:
                return par[n]
            par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            n1, n2 = find(n1), find(n2)
            if n1 == n2:
                return False
            if rank[n1] > rank[n2]:
                par[n2] = n1
                rank[n1] += rank[n2]
            else:
                par[n1] = n2
                rank[n2] += rank[n1]
            return True
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
