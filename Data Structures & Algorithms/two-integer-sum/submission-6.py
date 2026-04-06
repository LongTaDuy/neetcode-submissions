class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        for index, value in enumerate(nums):
            result.append([value, index])
        
        result.sort()

        left = 0
        right = len(nums) - 1
        ans = [0, 0]
        while left < right:
            if target - result[left][0] < result[right][0]:
                right -= 1
            elif target - result[left][0] > result[right][0]:
                left += 1
            else:
                ans[0] = min(result[left][1], result[right][1])
                ans[1] = max(result[left][1], result[right][1])
                break
        return ans