class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0 : 1}
        cursum = 0
        res = 0
        for i in range(len(nums)):
            cursum += nums[i]
            diff = cursum - k
            res += freq.get(diff, 0)
            freq[cursum] = freq.get(cursum, 0) + 1
        return res



