class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    for dr, dc in directions:
                        row, col = r + dr, c + dc
                        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                            res += 1
        return res
            

                