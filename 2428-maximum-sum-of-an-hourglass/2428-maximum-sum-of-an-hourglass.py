class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        """
        ans = -10e4
        print(len(grid), len(grid[0]))
        for i in range(len(grid)):
            for k in range(len(grid[i])):
                if not (i + 2 < len(grid)):
                    continue
                temp = list()
                for j in range(k, k + 3):
                    if not (j < len(grid[i])):
                        continue
                    temp.append(grid[i][j])
                for idx, j in enumerate(range(k, k + 3)):
                    if not (j < len(grid[i + 1])):
                        continue
                    if idx == 0 or idx + 1 == i + 3:
                        continue
                    temp.append(grid[i + 1][j])
                for j in range(k, k + 3):
                    if not (j < len(grid[i + 2])):
                        continue
                    temp.append(grid[i + 2][j])
                    
                print(len(temp))
                if len(temp) == 7:
                    ans = max(sum(temp), ans)
        return ans
        """
        ans =  -10e4
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                temp = list()
                if not (i + 2 < len(grid)) or not (j + 2 < len(grid[i])):
                    continue
                temp.append(grid[i][j])
                temp.append(grid[i][j + 1])
                temp.append(grid[i][j + 2])
                temp.append(grid[i + 1][j + 1])
                temp.append(grid[i + 2][j])
                temp.append(grid[i + 2][j + 1])
                temp.append(grid[i + 2][j + 2])
                ans = max(sum(temp), ans)
        return ans
        # https://leetcode.com/problems/maximum-sum-of-an-hourglass/discuss/2678195/Python-Elegant-and-Short