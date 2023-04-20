class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for line in grid:
            ans += sum([1 for x in line if x < 0])
        return ans