class Solution:
    import math
    def reverse(self, x: int) -> int:
        max_int32, min_int32 = math.pow(2, 31) - 1, -math.pow(2, 31)
        x = int(str(x)[::-1]) if x >= 0 else int(str(x)[::-1][:-1]) * -1 
        return 0 if not (min_int32 < x and x < max_int32) else x
        
        