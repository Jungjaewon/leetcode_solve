class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        if n == 1:
            return True
        elif n == 0 :
            return False
        else:
            while n != 1:
                if n % 3 != 0:
                    return False
                else:
                    n = n // 3
            return True
        """
        if n == 1:
            return True
        elif n == 0 or n == -1:
            return False
        elif n < 0:
            return False
        else:
            power = round(math.log(abs(n),3))
            return 3 ** power == n