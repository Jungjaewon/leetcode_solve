class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        """
        ans = [ [0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                one_row, one_col = 0, 0
                for k in range(len(grid[i])):
                    one_row += grid[i][k]
                for k in range(len(grid)):
                    one_col += grid[k][j]
                ans[i][j] = one_row + one_col - (len(grid) - one_row) - (len(grid[i]) - one_col)
                #print(i,j, one_row, one_col, (len(grid) - one_row), (len(grid[i]) - one_col), ans[i][j])
        return ans
        """
        ans = [[0] * len(grid[0]) for _ in range(len(grid))]
        row_sum = [sum(line) for line in grid]
        col_sum = [sum(line) for line in zip(*grid)]
        for i in range(len(row_sum)):
            for j in range(len(col_sum)):
                ans[i][j] = row_sum[i] + col_sum[j] - (len(grid) - row_sum[i]) - (len(grid[i]) - col_sum[j])
        return ans