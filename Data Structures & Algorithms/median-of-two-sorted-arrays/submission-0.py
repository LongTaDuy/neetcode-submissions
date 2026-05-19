class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = []
        f1, f2 = 0, 0
        while f1 <= len(nums1) - 1 and f2 <= len(nums2) - 1:
            if nums1[f1] <= nums2[f2]:
                merge.append(nums1[f1])
                f1 += 1
            else:
                merge.append(nums2[f2])
                f2 += 1
        if f1 < len(nums1):
            while f1 < len(nums1):
                merge.append(nums1[f1])
                f1 += 1
        if f2 < len(nums2):
            while f2 < len(nums2):
                merge.append(nums2[f2])
                f2 += 1
        if len(merge) % 2 == 0:
            mid1 = merge[(len(merge)) // 2]
            mid2 = merge[(len(merge)) // 2 - 1]
            return (mid1 + mid2) / 2
        else:
            mid = merge[(len(merge)) // 2] 
            return mid