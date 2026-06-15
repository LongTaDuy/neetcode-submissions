class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def backtrack(i, cursum):
            if i >= len(nums):
                return 1 if cursum == target else 0
            if (i, cursum) in dp:
                return dp[(i, cursum)]

            dp[(i, cursum)] = backtrack(i + 1, cursum + nums[i]) + backtrack(i + 1, cursum - nums[i])
            return dp[(i, cursum)]
        return backtrack(0, 0)