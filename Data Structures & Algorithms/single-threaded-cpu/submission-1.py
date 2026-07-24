class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        res = []
        i = 0
        time = tasks[0][0]
        while heap or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i += 1
            if not heap:
                time = tasks[i][0]
            else:
                proctime, ans = heapq.heappop(heap)
                time += proctime
                res.append(ans)
        return res
            
