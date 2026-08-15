class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res | i
        return res * 2 ** (len(nums) - 1)