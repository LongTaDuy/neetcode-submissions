class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            hashmap[n] = i
        for i, n in enumerate(nums):
            val = target - n
            if val in hashmap and hashmap[val] != i:
                return [i, hashmap[val]]
        return [] 