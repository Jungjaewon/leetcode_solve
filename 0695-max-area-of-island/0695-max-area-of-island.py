class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
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
        