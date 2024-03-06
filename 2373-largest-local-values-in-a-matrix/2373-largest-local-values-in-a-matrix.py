class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        l=len(grid)-2
        ans=[]
        for i in range(l):
            ans.append([0]*l)
        for i in range(l):
            for j in range(l):
                ans[i][j] = max(grid[i][j],grid[i][j+1],grid[i][j+2],
                      grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],
                      grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2])
        return ans
    # https://leetcode.com/problems/largest-local-values-in-a-matrix/discuss/2422088/C%2B%2B-or-Simple-solution-or-O(n2)
    # https://leetcode.com/problems/largest-local-values-in-a-matrix/discuss/2694982/Easy
                