class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
        #https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
        """
        m, n = len(matrix), len(matrix[0])
        visited, ans = [[False] * n for _ in range(m)], list()
        dir_dict = {0 : [0,1], 1 : [1, 0], 2 : [0, -1], 3 : [-1, 0]}
        ch_dict = {0 : 1, 1 : 2, 2 :3, 3: 0}
        cur_dir, x, y, cnt = 0, 0, 0, 0
        while cnt < m * n:
            #print(f'x : {x}, y : {y}')
            visited[x][y] = True
            ans.append(matrix[x][y])
            
            dx, dy = dir_dict[cur_dir]
            nx, ny = x + dx, y + dy
            
            if -1 < nx and nx < m and -1 < ny and ny < n and not visited[nx][ny]:
                x, y = nx, ny
            else:
                cur_dir = ch_dict[cur_dir]
                dx, dy = dir_dict[cur_dir]
                x, y = x + dx, y + dy
            
            cnt += 1
        return ans
        """
        