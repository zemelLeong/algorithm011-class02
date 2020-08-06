class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [item + [float('inf')] for item in grid] + [[float('inf')] * (len(grid[0]) + 1)]
        dp[-1][-2], dp[-2][-1] = 0, 0
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                dp[row][col] += min((dp[row + 1][col], dp[row][col + 1]))
        return dp[0][0]