class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[0])
        res = 0
        curend = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= curend:
                curend = end
            else:
                res += 1
                curend = min(curend, end)
        return res
            