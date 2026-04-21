class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}
        ans = 0
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                ans = nums[i]
        return ans