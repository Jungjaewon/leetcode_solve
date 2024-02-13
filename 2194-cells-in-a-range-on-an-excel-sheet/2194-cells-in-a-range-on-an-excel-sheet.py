class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(':')
        s_s, s_d = start[0], int(start[1])
        e_s, e_d = end[0], int(end[1])
        ans = list()
        for r in range(ord(s_s), ord(e_s) + 1):
            for c in range(s_d, e_d + 1): 
                ans.append(f'{chr(r)}{c}')
        return ans
        