class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        if n == 1:
            return True
        elif n == 0 :
            return False
        else:
            while n != 1:
                if n % 2 != 0:
                    return False
                else:
                    n = n // 2
            return True
        """
        if n <= 0:
            return False
        
        power = round(math.log(n, 2))
        return 2 ** power == n
                    