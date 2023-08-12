class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        s = int(sqrt(num))
        return s * s == num
        """
        return int(sqrt(num)) * int(sqrt(num)) == num