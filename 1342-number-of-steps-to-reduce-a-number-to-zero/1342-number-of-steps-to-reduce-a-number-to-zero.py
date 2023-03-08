class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num != 0:
            num = num // 2 if num & 1 == 0 else num -1
            ans += 1
        return ans