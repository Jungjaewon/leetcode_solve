class Solution:
    def checkZeroOnes(self, s: str) -> bool:    
        def func(s, n='1'):
            max_v, cnt = 0, 0
            for c in s:
                if c == n:
                    cnt += 1
                else:
                    max_v = max(max_v, cnt)
                    cnt = 0
            max_v = max(max_v, cnt)
            return max_v
        return func(s,'1') > func(s,'0')
    
            