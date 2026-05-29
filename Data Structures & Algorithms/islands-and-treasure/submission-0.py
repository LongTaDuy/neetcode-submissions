class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r, c) not in visited:
                    q.append((r, c))
                    visited.add((r, c))
        def addroom(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == -1 or (r, c) in visited:
                return
            visited.add((r, c))
            q.append((r, c))
        dist = 0

        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                addroom(row + 1, col)
                addroom(row - 1, col)
                addroom(row, col + 1)
                addroom(row, col - 1)
            dist += 1

            

