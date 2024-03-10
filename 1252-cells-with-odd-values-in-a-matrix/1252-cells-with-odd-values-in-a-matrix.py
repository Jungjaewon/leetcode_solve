class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        ans = 0
        arr = [ [0] * n  for _ in range(m)]
        
        for i in range(len(indices)):
            r,c = indices[i]
            for j in range(n):
                arr[r][j] += 1
            for j in range(m):
                arr[j][c] += 1
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] & 1 == 1:
                    ans += 1
        return ans