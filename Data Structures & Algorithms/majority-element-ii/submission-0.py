class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 0979096550
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        res = []
        for key, value in freq.items():
            if value > len(nums) / 3:
                res.append(key)
        return res