class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l, r = 1, length - 2
        peak = 0
        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)
            left = mountainArr.get(mid - 1)
            right = mountainArr.get(mid + 1)
            if left < val and val < right:
                l = mid + 1
            elif right < val and val < left:
                r = mid - 1
            else:
                peak = mid
                break
        #left
        l, r = 0, peak - 1
        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)
            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return mid
        # right
        l, r = peak, length - 1
        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)
            if val < target:
                r = mid - 1
            elif val > target:
                l = mid + 1
            else:
                return mid
        return -1
