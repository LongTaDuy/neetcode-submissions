class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2
            sum_hour = 0

            for pile in piles:
                sum_hour += (pile + mid - 1) // mid

            if sum_hour <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res

