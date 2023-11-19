class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0 :
            return False
        else:
            while n != 1:
                if n % 4 != 0:
                    return False
                else:
                    n = n // 4
            return True
        """
        if n <= 0:
            return False
        
        power = round(math.log(n, 4))
        return 4 ** power == n
        """