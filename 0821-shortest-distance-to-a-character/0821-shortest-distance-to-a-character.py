class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_set = {idx for idx, k in enumerate(s) if k == c} 
        return [ 0 if k == c else min([ abs(c_idx - i) for c_idx in c_set]) for i, k in enumerate(s)]
            