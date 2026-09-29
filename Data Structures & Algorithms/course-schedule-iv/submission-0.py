class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)
        premap = {}
        def dfs(course):
            if course not in premap:
                premap[course] = set()
                for prereq in adj[course]:
                    premap[course] = premap[course] | dfs(prereq)
                premap[course].add(course)
            return premap[course]

        for course in range(numCourses):
            dfs(course)
        res = []
        for u, v in queries:
            if u in premap[v]:
                res.append("true")
            else:
                res.append("false")
        return res

        