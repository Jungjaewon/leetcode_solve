class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [-10e4] * n
        for row in grid:
            for r_idx, n in enumerate(row):
                ans[r_idx] = max(len(str(n)), ans[r_idx])
        return ans