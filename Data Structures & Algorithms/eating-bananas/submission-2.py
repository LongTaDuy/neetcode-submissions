class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def count_banana(k):
            hours = 0
            for i in piles:
                hours += (i + k - 1) // k
            return hours <= h
        left, right = 1, max(piles)
        res = right
        while left <= right:
            mid = (left + right) // 2
            if count_banana(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

