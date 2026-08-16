class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[rows - 1][cols - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * (cols + 1) for i in range(rows + 1)]
        dp[rows - 1][cols - 1] = 1
        visited = set()
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] += dp[r + 1][c] + dp[r][c + 1]
        return dp[0][0]