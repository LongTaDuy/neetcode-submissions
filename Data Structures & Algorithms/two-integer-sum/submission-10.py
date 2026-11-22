class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i in range(len(nums)):
            index[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in index and index[target - nums[i]] != i:
                return [i, index[target - nums[i]]]
        