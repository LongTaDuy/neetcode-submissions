class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for i in range(len(nums) + 1)]
        res = []
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for key, val in freq.items():
            bucket[val].append(key)
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

