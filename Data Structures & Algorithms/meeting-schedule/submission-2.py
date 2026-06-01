"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start)
        for i in range(1, len(intervals)):
            cur = intervals[i]
            pre = intervals[i - 1]
            if cur.start < pre.end:
                return False
        return True