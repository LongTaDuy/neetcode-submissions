class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for x, y in points:
            dist = (x**2 + y**2)
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)
        for i in range(k):
            ans = heapq.heappop(minHeap)
            res.append([ans[1], ans[2]])
        return res