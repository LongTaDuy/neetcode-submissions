class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        row = defaultdict(list)
        col = defaultdict(list)
        square = defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r // 3, c // 3)]:
                    return False
                row[r].append(board[r][c])
                col[c].append(board[r][c])
                square[(r // 3), (c // 3)].append(board[r][c])
        return True

