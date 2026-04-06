class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tich = 1
        result = []
        for i in range(0, len(nums)):
            if nums[i] == 0:
                tich *= 1
            else:
                tich *= nums[i]
        count = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                count += 1
        for i in range(0, len(nums)):
            ans = 0
            if nums[i] == 0 and count == 1:
                ans = tich
            elif nums[i] != 0 and count > 0:
                ans = 0
            elif nums[i] != 0 and count == 0:
                ans = int(tich / nums[i])
            result.append(ans)
        return result