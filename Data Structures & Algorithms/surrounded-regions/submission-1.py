class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            while q:
                row, col = q.popleft()
                direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in direction:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and board[r][c] == 'O' and (r, c) not in visited:
                        board[r][c] = 'T'
                        q.append((r, c))
                        visited.add((r, c))
            
        for r in range(rows):
            if board[r][0] == 'O' and (r, 0) not in visited:
                board[r][0] = 'T'
                bfs(r, 0)
            if board[r][cols - 1] == 'O' and (r, cols - 1) not in visited:
                board[r][cols - 1] = 'T'
                bfs(r, cols - 1)
        for c in range(cols):
            if board[0][c] == 'O' and (0, c) not in visited:
                board[0][c] = 'T'
                bfs(0, c)
            if board[rows - 1][c] == 'O' and (rows - 1, c) not in visited:
                board[rows - 1][c] = 'T'
                bfs(rows - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'


