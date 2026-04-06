class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        left = 0
        right = len(numbers) - 1
        while left < right:
            if target - numbers[left] < numbers[right]:
                right -= 1
            elif target - numbers[left] > numbers[right]:
                left += 1
            else:
                result.append(min(left + 1, right + 1))
                result.append(max(left + 1, right + 1))
                break
        return result