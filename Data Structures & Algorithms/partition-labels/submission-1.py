class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex = {}
        for index, value in enumerate(s):
            lastindex[value] = index
        
        size, end = 0, 0
        res = []
        for i in range(len(s)):
            end = max(end, lastindex[s[i]])
            size += 1
            if i == end:
                res.append(size)
                size = 0
        return res
            
            

            