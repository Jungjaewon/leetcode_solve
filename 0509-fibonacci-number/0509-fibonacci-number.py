class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a,b,c = 0, 1, 0
            for _ in range(n - 1):
                c = a + b
                print(f'c : {c}')
                a, b = b, c
            return c