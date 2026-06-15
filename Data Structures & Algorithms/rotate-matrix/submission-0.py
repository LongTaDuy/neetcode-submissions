class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            top, bottom = l, r
            for i in range(r - l):
                topleft = matrix[top][top + i]
                matrix[top][top + i] = matrix[bottom - i][top]
                matrix[bottom - i][top] = matrix[bottom][bottom - i]
                matrix[bottom][bottom - i] = matrix[top + i][bottom]
                matrix[top + i][bottom] = topleft
            l += 1
            r -= 1