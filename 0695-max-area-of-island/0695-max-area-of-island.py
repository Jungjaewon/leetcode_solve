class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir_xy, ans = [[0,1],[0,-1],[1,0],[-1,0]], [-10e4]
        m, n  = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        def dfs(x,y):
            temp_area[0] += 1
            visited[x][y] = True
            for dx, dy in dir_xy:
                nx, ny = x + dx, y + dy
                if -1 < nx and nx < m and -1 < ny and ny < n and not visited[nx][ny] and grid[nx][ny] == 1:
                    dfs(nx, ny)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == False:
                    visited[i][j], temp_area = True, [0]
                    dfs(i, j)
                    ans[0] = max(ans[0], temp_area[0])
        return ans[0] if ans[0] != -10e4 else 0
                    
        """
        from queue import Queue
        ans = [-10e4]
        dir_xy = [[0,1],[0,-1],[1,0],[-1,0]]
        m, n  = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == False:
                    Q, temp_area = Queue(), 0
                    Q.put([i, j])
                    visited[i][j] = True
                    while Q.qsize():
                        tx, ty = Q.get()
                        temp_area += 1
                        for dx, dy in dir_xy:
                            nx, ny = tx + dx, ty + dy
                            if -1 < nx and nx < m and -1 < ny and ny < n and grid[nx][ny] == 1 and visited[nx][ny] == False:
                                Q.put([nx, ny])
                                visited[nx][ny] = True
                    ans[0] = max(ans[0], temp_area)
        return ans[0] if ans[0] != -10e4 else 0
        """