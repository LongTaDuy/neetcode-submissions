class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1 
        sum = 0
        while l < r:
            heights = min(height[l], height[r])
            if heights == height[l]:
                if height[l] < height[l + 1]:
                    l = l + 1
                else:
                    l_check = l
                    while l_check < r and height[l_check] <= height[l]:
                        sum += heights - height[l_check]
                        l_check += 1
                    l = l_check
            else:
                if height[r] < height[r - 1]:
                    r = r - 1
                else:
                    r_check = r
                    while r_check > l and height[r_check] <= height[r]:
                        sum += heights - height[r_check]
                        r_check -= 1
                    r = r_check
        return sum


