class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(num):
            cursum = 0
            sub = 1
            for i in nums:
                cursum += i
                if cursum > num:
                    sub += 1
                    cursum = 0
                    if sub > k:
                        return False
                    cursum = i
            return True
        l, r = max(nums), sum(nums)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if cansplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
