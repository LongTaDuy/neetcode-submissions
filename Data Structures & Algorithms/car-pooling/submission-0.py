class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minheap = [] # [end, numPass]
        trips.sort(key=lambda x: x[1])
        curPass = 0
        for numPass, start, end in trips:
            while minheap and start >= minheap[0][0]:
                curPass -= heapq.heappop(minheap)[1]
            curPass += numPass
            if curPass > capacity:
                return False
            heapq.heappush(minheap, [end, numPass])
        return True
