class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        def checkw(w):
            cur = 0
            day = 1
            for i in weights:
                if cur + i > w:
                    day += 1
                    cur = 0
                cur += i
            return day <= days
        res = right
        while left <= right:
            mid = (left + right) // 2
            if checkw(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res


