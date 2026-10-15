class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, n):
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n
    def union(self, n1, n2):
        n1, n2 = self.find(n1), self.find(n2)
        if n1 == n2:
            return False
        if self.rank[n1] > self.rank[n2]:
            self.par[n2] = n1
            self.rank[n1] += self.rank[n2]
        else:
            self.par[n1] = n2
            self.rank[n2] += self.rank[n1]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i) # [v1, v2, w, i]
        edges.sort(key=lambda e: e[2])
        mst_weight = 0
        uf = UnionFind(n)
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mst_weight += w
        critical, pseudo = [], []
        for v1, v2, w, i in edges:
            # critical - without the cur edge
            weight = 0
            uf = UnionFind(n)
            for n1, n2, cur_w, j in edges:
                if i != j and uf.union(n1, n2):
                    weight += cur_w
            if max(uf.rank) != n or weight > mst_weight:
                critical.append(i)
                continue
            # pseudo - with the cur edge
            uf = UnionFind(n)
            uf.union(v1, v2)
            weight = w
            for n1, n2, cur_w, j in edges:
                if uf.union(n1, n2):
                    weight += cur_w
            if weight == mst_weight:
                pseudo.append(i)
        return [critical, pseudo]




        