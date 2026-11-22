class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storage = {}
        for i in nums:
            if i in storage:
                return True
            else:
                storage[i] = 1
        return False