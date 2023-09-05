class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for n in range(low, high + 1):
            s_n = str(n)
            if len(s_n) & 1 == 0:
                left = sum([int(i) for i in s_n[:len(s_n)// 2]])
                right = sum([int(i) for i in s_n[len(s_n)// 2:]])
                ans = ans + 1 if left == right else ans
        return ans