class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s_num, divisor, ans = str(num), list(), 0
        for i in range(len(s_num) - k + 1):
            divisor.append(s_num[i: i + k])
        for d in divisor:
            if int(d) != 0 and num % int(d) == 0:
                ans += 1
        return ans
    