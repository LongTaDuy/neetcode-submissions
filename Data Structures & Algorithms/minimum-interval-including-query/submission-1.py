class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = {}
        minheap = []
        intervals.sort()
        i = 0
        heapq.heapify(minheap)
        for n in sorted(queries):
            while i < len(intervals) and n >= intervals[i][0]:
                l, r = intervals[i][0], intervals[i][1]
                heapq.heappush(minheap, [r - l + 1, r])
                i += 1
            
            while minheap and minheap[0][1] < n:
                heapq.heappop(minheap)
            res[n] = minheap[0][0] if minheap else -1
        ans = []
        for n in queries:
            ans.append(res[n])
        return ans

