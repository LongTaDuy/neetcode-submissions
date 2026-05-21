class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        map = Counter(tasks)
        maxheap = [-cnt for cnt in map.values()]
        heapq.heapify(maxheap)
        queue = deque() 
        time = 0
        while maxheap or queue:
            time += 1
            if not maxheap:
                time = queue[0][1]
            else:
                cnt = 1 + heapq.heappop(maxheap)
                if cnt:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxheap, queue.popleft()[0])
        return time
        
