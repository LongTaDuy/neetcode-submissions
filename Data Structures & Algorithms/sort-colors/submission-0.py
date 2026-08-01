class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colors = [0] * 3
        for num in nums:
            colors[num] += 1
        index = 0
        for i in range(3):
            while colors[i]:
                nums[index] = i
                colors[i] -= 1
                index += 1
