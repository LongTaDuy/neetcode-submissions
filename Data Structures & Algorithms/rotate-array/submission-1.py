class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[(i + k) % len(nums)] = nums[i]
        nums[:] = res