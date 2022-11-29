class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m - 1 + n - 1) // (math.factorial(m - 1) * math.factorial(n - 1))
        """
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            ans[i][0] = 1
        
        for j in range(n):
            ans[0][j] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                ans[i][j] = ans[i -1][j] + ans[i][j - 1]
        return ans[m - 1][n - 1]
        """
        """
        from queue import Queue
        Q, ans = Queue(), 0
        Q.put([0, 0])
        
        while Q.qsize():
            x, y = Q.get()
            
            ans = ans + 1 if x == m - 1 and y == n - 1 else ans
            
            for dx, dy in [[1,0],[0,1]]:
                nx, ny = x + dx, y + dy
                if -1 < nx and nx < m and -1 < ny and ny < n:
                    Q.put([nx, ny])
        return ans
        """