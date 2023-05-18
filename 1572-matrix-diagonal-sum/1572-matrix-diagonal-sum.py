class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n, ans = len(mat), 0
        sx, sy, ex, ey = 0, 0, 0, n - 1
        
        if sx == ex and sy == ey:
            return mat[sx][sy]
        else:
            while sx < n and sy < n:
                ans += mat[sx][sy]
                #print(mat[sx][sy])
                sx, sy = sx + 1, sy + 1
            while ex < n and -1 < ey:
                ans += mat[ex][ey]
                #print(mat[ex][ey])
                ex, ey = ex + 1, ey - 1
            #print(f'-',mat[n - 1][n - 1])
            if n & 1 == 1:
                idx = (n // 2)
                #print(idx)
                ans -= mat[idx][idx]
            return ans 
                
        
        