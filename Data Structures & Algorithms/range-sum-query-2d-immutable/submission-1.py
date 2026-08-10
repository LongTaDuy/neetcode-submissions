class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.matsum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                self.matsum[r + 1][c + 1] = prefix + self.matsum[r][c + 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = self.matsum[row1][col2 + 1]
        left = self.matsum[row2 + 1][col1]
        topleft = self.matsum[row1][col1]
        return self.matsum[row2 + 1][col2 + 1] - top - left + topleft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)