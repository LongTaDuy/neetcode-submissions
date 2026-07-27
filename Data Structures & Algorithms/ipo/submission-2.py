class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minheap = []
        for index, cap in enumerate(capital):
            heapq.heappush(minheap, [cap, index, profits[index]])
        res = w
        maxheap = [] # [profit]
        while k:
            while minheap and res >= minheap[0][0]:
                cap, index, profit = heapq.heappop(minheap)
                heapq.heappush(maxheap, -profit)
            if not maxheap:
                break
            profit = heapq.heappop(maxheap)
            res += (-profit)
            k -= 1
        return res
            
