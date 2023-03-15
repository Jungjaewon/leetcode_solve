class Solution:
    def countDigits(self, num: int) -> int:
        """
        ans = 0
        for n in list(str(num)):
            if num % int(n) == 0:
                ans += 1
        return ans
        """
        #return sum([1 for n in list(str(num)) if num % int(n) == 0])
        temp, ans = num, 0
        while temp:
            n = temp % 10
            ans = ans + 1 if num % n == 0 else ans
            temp = temp // 10
        return ans