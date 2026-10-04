class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, x: int):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self, x1: int, x2: int):
        x1, x2 = self.find(x1), self.find(x2)
        if x1 == x2:
            return False
        if self.rank[x1] > self.rank[x2]:
            self.par[x2] = x1
            self.rank[x1] += self.rank[x2]
        else:
            self.par[x1] = x2
            self.rank[x2] += self.rank[x1]
        return True
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToIndex = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToIndex:
                    uf.union(i, emailToIndex[e])
                else:
                    emailToIndex[e] = i
        indexToAccount = defaultdict(list)
        for e, i in emailToIndex.items():
            leader = uf.find(i)
            indexToAccount[leader].append(e)
        res = []
        for i, emails in indexToAccount.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))
        return res
        





        