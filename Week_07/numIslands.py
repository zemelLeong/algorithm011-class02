class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, ans = len(grid), 0
        if rows == 0: return 0
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '0': continue
                ans += 1
                self.dfs(row, col, grid)
        return ans

    def dfs(self, row, col, grid):
        if -1 < row < len(grid) and -1 < col < len(grid[0]) and grid[row][col] == '1':
            grid[row][col] = '0'
            for x, y in ((1, 0), (0, 1), (-1, 0), (0, -1)): self.dfs(row + x, col + y, grid)