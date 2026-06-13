class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for i in queries:
            minheap = []
            for j in range(len(intervals)):
                left, right = intervals[j]
                if left <= i <= right:
                    minheap.append(right - left + 1)
            if minheap:
                heapq.heapify(minheap)
                res.append(minheap[0])
            else:
                res.append(-1)
        return res
