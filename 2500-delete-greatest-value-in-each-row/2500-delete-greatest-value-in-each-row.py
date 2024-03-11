class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid[0])
        while n > 0:
            temp_a = list()
            for idx,row in enumerate(grid):
                #print(row)
                max_v, m_idx = 0,0
                for cidx, v in enumerate(row):
                    if v > max_v:
                        max_v = v
                        m_idx = cidx
                del grid[idx][m_idx]
                temp_a.append(max_v)
            ans += max(temp_a)
            n -= 1
        
        return ans
            
            
            