class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            a, b, c, d = 0, 1, 1, 0
            for i in range(n - 2):
                d = a + b + c
                a,b,c = b,c,d
            return d
        
        """
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)
        """
        
        