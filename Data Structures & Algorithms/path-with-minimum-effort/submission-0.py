class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        min_heap = [(0, 0, 0)] # diff, row, col
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while min_heap:
            diff, row, col = heapq.heappop(min_heap)
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if row == rows - 1 and col == cols - 1:
                return diff
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or (r, c) in visited):
                    continue
                new_diff = max(diff, abs(heights[r][c] - heights[row][col]))
                heapq.heappush(min_heap, (new_diff, r, c))
        return 0