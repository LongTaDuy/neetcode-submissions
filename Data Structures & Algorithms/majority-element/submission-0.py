class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        maxcount = res = 0
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
            if maxcount < freq[i]:
                maxcount = freq[i]
                res = i
        return res
        
