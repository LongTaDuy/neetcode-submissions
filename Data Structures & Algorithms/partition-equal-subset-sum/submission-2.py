class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        dp = set()
        target = sum(nums) // 2
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            nextdp = set()
            for t in dp:
                nextdp.add(nums[i] + t)
                nextdp.add(t)
            dp = nextdp
        return True if target in dp else False
