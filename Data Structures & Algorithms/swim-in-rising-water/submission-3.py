class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        min_heap = [(grid[0][0], 0, 0)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        while min_heap:
            heights, row, col = heapq.heappop(min_heap)
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if row == rows - 1 and col == cols - 1:
                return heights
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r < 0 or r > rows - 1 or c < 0 or c > rows - 1 or (r, c) in visited):
                    continue
                new_heights = max(heights, grid[r][c])
                heapq.heappush(min_heap, (new_heights, r, c))
        return 0
            