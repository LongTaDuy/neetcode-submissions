class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for key, val in freq.items():
            heapq.heappush(res, [val, key])
            if len(res) > k:
                heapq.heappop(res)
        ans = []
        for _ in range(k):
            val, key = heapq.heappop(res)
            ans.append(key)
        return ans
