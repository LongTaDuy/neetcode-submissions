class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for i in tasks:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        maxheap = [-c for c in freq.values()]
        heapq.heapify(maxheap)
        q = deque() # [-cnt, readytime]
        time = 0
        while q or maxheap:
            time += 1
            if not maxheap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time


