class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        result = []

        for i in range(0, len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1

  
        sortdic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}
        for key, value in reversed(sortdic.items()):
            if k > 0:
                result.append(key)
                k -= 1
            else:
                break
        return result