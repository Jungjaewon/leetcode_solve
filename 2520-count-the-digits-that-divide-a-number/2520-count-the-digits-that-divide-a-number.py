class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        for n in list(str(num)):
            if num % int(n) == 0:
                ans += 1
        return ans