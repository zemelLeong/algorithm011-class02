class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.pos = []
        self.helper([], [], [], n)
        return [["." * j + "Q" + "." * (n - j - 1) for j in i] for i in self.pos]

    def helper(self, queens, att_left, att_right, n):
        row = len(queens)
        if row >= n:
            self.pos.append(queens)
            return
        for col in range(n):
            left, right = row + col, col - row
            if left in att_left or col in queens or right in att_right: continue
            self.helper(queens + [col], att_left + [left], att_right + [right], n)