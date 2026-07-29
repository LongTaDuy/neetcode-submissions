class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False] * len(nums)
        def backtrack(path):
            if len(nums) == len(path):
                if path not in res:
                    res.append(path.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    path.append(nums[i])
                    pick[i] = True
                    backtrack(path)
                    path.pop()
                    pick[i] = False
        backtrack([])
        return res