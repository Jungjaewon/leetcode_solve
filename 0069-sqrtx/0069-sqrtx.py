class Solution:
    def mySqrt(self, x: int) -> int:
        """
        import math
        return int(math.sqrt(x))
        """            
        for i in range(0, x + 1):
            if (i * i) == x:
                return i
            elif (i * i) > x:
                return i - 1