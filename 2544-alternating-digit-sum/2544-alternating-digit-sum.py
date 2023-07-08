class Solution:
    def alternateDigitSum(self, n: int) -> int:
        #return sum([ int(x) if idx & 1 == 0 else -int(x) for idx, x in enumerate(str(n))])
        ans = 0 
        for idx, x in enumerate(str(n)):
            if idx & 1 == 0:
                ans += int(x)
            else:
                ans -= int(x)
        return ans