class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(1, n + 2):
            r = i * n
            if r % 2 == 0 and r > 1:
                return r