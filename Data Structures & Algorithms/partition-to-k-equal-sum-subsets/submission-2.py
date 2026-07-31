class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        used = [0] * k
        target = sum(nums) // k
        nums.sort(reverse=True)
        def backtrack(i):
            if i == len(nums):
                return True
            for j in range(len(used)):
                if nums[i] + used[j] > target:
                    continue
                if j > 0 and used[j] == used[j - 1]:
                    continue
                used[j] += nums[i]
                if backtrack(i + 1):
                    return True
                used[j] -= nums[i]
            return False
        return backtrack(0)




                