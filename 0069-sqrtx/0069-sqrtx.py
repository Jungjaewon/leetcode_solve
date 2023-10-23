class Solution:
    def mySqrt(self, x: int) -> int:
        """
        import math
        return int(math.sqrt(x))
        """            
        """
        for i in range(0, x + 1):
            if (i * i) == x:
                return i
            elif (i * i) > x:
                return i - 1
        """
        for i in range(0, x + 1):
            ret = (i * i)
            if ret == x:
                return i
            elif ret > x:
                return i - 1