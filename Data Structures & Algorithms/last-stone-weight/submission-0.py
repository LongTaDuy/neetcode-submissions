class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            first = heapq.heappop(maxheap)
            second = heapq.heappop(maxheap)
            if second - first > 0:
                heapq.heappush(maxheap, first - second)
        maxheap.append(0)
        return abs(maxheap[0])