class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for i in nums:
            heapq.heappush(minheap, -i)
        while k > 1:
            heapq.heappop(minheap)
            k -= 1
        res = -heapq.heappop(minheap)
        return res
            
