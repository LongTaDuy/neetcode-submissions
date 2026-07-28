class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalmax, globalmin = nums[0], nums[0]
        curmax, curmin = 0, 0
        total = 0
        for i in nums:
            curmax = max(i, curmax + i)
            curmin = min(i, curmin + i)
            total += i
            globalmax = max(globalmax, curmax)
            globalmin = min(globalmin, curmin)
        return max(globalmax, total - globalmin) if globalmax > 0 else globalmax