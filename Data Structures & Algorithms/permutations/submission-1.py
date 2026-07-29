class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False] * len(nums)
        def backtrack(path, pick):
            if len(path) == len(nums):
                res.append(path.copy())
                return 
            for i in range(len(nums)):
                if not pick[i]:
                    path.append(nums[i])
                    pick[i] = True
                    backtrack(path, pick)
                    path.pop()
                    pick[i] = False
        backtrack([], pick)
        return res
            