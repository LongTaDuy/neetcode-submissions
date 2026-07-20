class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = sum(weights)
        def check(cap):
            ships, weight = 1, cap
            for i in weights:
                if weight - i < 0:
                    ships += 1
                    weight = cap
                weight -= i
            return ships <= days
        while l <= r:
            cap = (l + r) // 2
            if check(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res