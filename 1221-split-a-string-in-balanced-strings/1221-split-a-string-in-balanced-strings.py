class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans, R_cnt, L_cnt = 0, 0, 0
        for c in s:
            if c == 'L':
                L_cnt += 1
            elif c == 'R':
                R_cnt += 1
            if L_cnt == R_cnt:
                ans += 1
                R_cnt, L_cnt = 0, 0
        return ans
        
        