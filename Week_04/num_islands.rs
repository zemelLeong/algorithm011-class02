impl Solution {
    pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
        let rows = grid.len();
        if rows == 0 {return 0;}
        let cols = grid[0].len();
        let mut editable_grid = grid;
        let mut ans: i32 = 0;

        for row in 0..rows {
            for col in 0..cols {
                if editable_grid[row][col] == '1' {
                    ans += 1;
                    Self::dfs(row, col, &mut editable_grid);
                }
            }
        }
        ans
    }

    fn dfs(row: usize, col: usize, grid: &mut Vec<Vec<char>>) {
        if row < 0 || col < 0 || row >= grid.len() || col >= grid[0].len() || grid[row][col] == '0' {return;}

        grid[row][col] = '0';
        // 上
        Self::dfs(row - 1, col, grid);
        // 右
        Self::dfs(row, col + 1, grid);
        // 下
        Self::dfs(row + 1, col, grid);
        // 左
        Self::dfs(row, col - 1, grid);
    }
}