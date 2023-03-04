class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return reduce(lambda a,b: a*b, [int(c) for c in str(n)]) - sum([int(c) for c in str(n)])