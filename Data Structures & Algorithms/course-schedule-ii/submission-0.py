class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visit, cycle = set(), set()
        res = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for c in adj[crs]:
                if dfs(c) == False:
                    return False
            
            visit.add(crs)
            cycle.remove(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return res