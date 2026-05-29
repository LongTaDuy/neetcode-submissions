class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2 and (r, c) not in visited:
                    q.append((r, c))
                    visited.add((r, c))
        
        def bfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] != 1 or (r, c) in visited:
                return 
            q.append((r, c))
            visited.add((r, c))
        
        cnt = -1
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = 2
                bfs(row + 1, col)
                bfs(row - 1, col)
                bfs(row, col + 1)
                bfs(row, col - 1)
            cnt += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        if cnt == -1:
            return 0
        return cnt


