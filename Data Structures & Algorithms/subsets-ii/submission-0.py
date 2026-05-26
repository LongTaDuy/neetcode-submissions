class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def backtrack(start):
            if start >= len(nums):
                res.append(subset.copy())
                return
            # add cur
            subset.append(nums[start])
            backtrack(start + 1)
            subset.pop()
            # not add
            while start + 1 < len(nums) and nums[start] == nums[start + 1]:
                start += 1
            backtrack(start + 1)

        backtrack(0)
        return res