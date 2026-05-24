class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin, curmax = 1, 1
        for i in nums:
            if i == 0:
                curmin, curmax = 1, 1
                continue
            tmp = curmin * i
            curmin = min(i * curmin, i * curmax, i)
            curmax = max(i * curmax, tmp, i)
            res = max(res, curmax)
        return res
        
        
            