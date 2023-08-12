class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s = int(sqrt(num))
        return s * s == num