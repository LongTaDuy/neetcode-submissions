class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        minheap = []
        for key, val in freq.items():
            heapq.heappush(minheap, [-val, key])
        while k > 0:
            val, key = heapq.heappop(minheap)
            res.append(key)
            k -= 1
        return res
