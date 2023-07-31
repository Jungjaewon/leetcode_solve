class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        """
        n, m = len(grid), len(grid[0])
        x,y = 0,0
        dig_list = list()
        while x < n and y < m:
            dig_list.append(f'{x}_{y}')
            x, y = x + 1, y + 1
        x,y = 0, m - 1
        while x < n and -1 < y:
            dig_list.append(f'{x}_{y}')
            x, y = x + 1, y - 1
        for i in range(n):
            for j in range(m):
                xy = f'{i}_{j}'
                if xy in dig_list and grid[i][j] > 0:
                    pass
                elif xy not in dig_list and grid[i][j] == 0:
                    pass
                else:
                    return False
        return True
        """
        """
        n, m = len(grid), len(grid[0])
        x,y = 0,0
        dig_list = list()
        while x < n and y < m:
            if grid[x][y] == 0:
                return False
            dig_list.append(f'{x}_{y}')
            x, y = x + 1, y + 1
        x,y = 0, m - 1
        while x < n and -1 < y:
            if grid[x][y] == 0:
                return False
            dig_list.append(f'{x}_{y}')
            x, y = x + 1, y - 1
        for i in range(n):
            for j in range(m):
                xy = f'{i}_{j}'
                if xy in dig_list:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] > 0:
                        return False
                    
        return True
        """
        n, m = len(grid), len(grid[0])
        x,y = 0,0
        dig_list = list()
        while x < n and y < m:
            if grid[x][y] == 0:
                return False
            dig_list.append(f'{x}_{y}')
            x, y = x + 1, y + 1
        x,y = 0, m - 1
        while x < n and -1 < y:
            if grid[x][y] == 0:
                return False
            dig_list.append(f'{x}_{y}')
            x, y = x + 1, y - 1
        for i in range(n):
            for j in range(m):
                xy = f'{i}_{j}'
                if xy in dig_list and grid[i][j] > 0:
                    pass
                elif xy not in dig_list and grid[i][j] == 0:
                    pass
                else:
                    return False
        return True
        
            