class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        res = ""
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1
        maxheap = [[-cnt, char] for char, cnt in freq.items()]
        heapq.heapify(maxheap)
        prev = None
        while maxheap or prev:
            if not maxheap and prev:
                return ""
            cnt, char = heapq.heappop(maxheap)
            res += char
            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            if cnt + 1 != 0:
                prev = [cnt + 1, char]
        return res