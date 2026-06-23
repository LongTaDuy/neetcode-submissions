class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minheap = [(grid[0][0], 0, 0)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        visited.add((0, 0))
        while minheap:
            time, r, c = heapq.heappop(minheap)
            if r == rows - 1 and c == cols - 1:
                return time
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited:
                    continue
                visited.add((row, col))
                heapq.heappush(minheap, (max(time, grid[row][col]), row, col))
        

