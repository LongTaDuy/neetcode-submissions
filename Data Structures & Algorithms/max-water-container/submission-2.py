class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            if heights[l] < heights[r]:
                res = max(heights[l] * (r - l), res)
                l += 1
            else:
                res = max(heights[r] * (r - l), res)
                r -= 1
        return res