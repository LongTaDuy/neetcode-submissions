class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            s.add(i)
        ans = 0
        for i in s:
            new_s = []
            cnt = 0
            result = 0
            if i - 1 not in s:
                new_s.append(i)
                result += 1
                check = True
                while check == True:
                    if new_s[cnt] + 1 in s:
                        new_s.append(new_s[cnt] + 1)
                        result += 1
                        cnt += 1
                    if new_s[cnt] + 1 not in s:
                        check = False
            ans = max(ans, result)
        return ans
            